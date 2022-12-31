from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from django.views import generic

from market.models import Cart, CartItem, WishList
from book.models import Book


class WishListAddService(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = WishList.objects.all()

    def post(self, request, book_id, *args, **kwargs):
        if not self.queryset.filter(
            profile=request.user, book_id=book_id, is_active=True
        ).exists():
            self.queryset.update_or_create(
                profile=request.user, book_id=book_id, is_active=True
            )
            return Response(
                {"message": "book added to wishlist"}, status=status.HTTP_200_OK
            )
        else:

            return Response(
                {"message": "It's already on the wish list"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class WishListView(generic.ListView):
    template_name = "pages/wishlist.html"
    queryset = WishList.objects.filter(is_active=True)


class WishListRemoveService(generics.DestroyAPIView):
    queryset = WishList.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, *args, **kwargs):
        try:
            wishlist = self.queryset.get(id=kwargs.get("pk"))
        except WishList.DoesNotExist:
            return Response(
                {"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        wishlist.is_active = False
        wishlist.save()
        return Response(
            {"message": "The book has been removed"}, status=status.HTTP_200_OK
        )


class CartAddService(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CartItem.objects.all()

    def post(self, request, *args, **kwargs):
        profile = request.user
        amount = int(request.data.get("amount"))
        book = request.data.get("id")
        book = Book.objects.get(id=book)

        if amount > book.amount:
            return Response(
                {"message": "Exceeded quantity of books in stock"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Cart.objects.filter(profile=profile).exists():
            cart = Cart.objects.get(profile=profile)
            if self.queryset.filter(book=book, profile=profile, cart=cart).exists():
                cart_item = self.queryset.get(book=book)
                new_amount = cart_item.amount + amount
                if new_amount > book.amount:
                    return Response(
                        {"message": "Exceeded quantity of books in stock"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                cart_item.amount = new_amount
                cart_item.price = new_amount * book.price
                cart_item.save()
            else:
                cart_item = self.queryset.create(
                    book=book,
                    profile=profile,
                    amount=amount,
                    cart=cart,
                    price=book.price * amount,
                )
        else:
            cart = Cart.objects.create(profile=profile)
            cart_item = self.queryset.create(
                book=book,
                profile=profile,
                amount=amount,
                cart=cart,
                price=book.price * amount,
            )
        cart.total += cart_item.price
        cart.save()

        return Response(
            {"message": "The book has been added to cart"}, status=status.HTTP_200_OK
        )


class CartView(generic.ListView):
    template_name = "pages/cart.html"
    queryset = Cart.objects.all()

    def get(self, request):
        context = {
            "items": CartItem.objects.filter(profile=request.user),
            "cart": self.queryset.get(profile=request.user),
        }

        return render(request, self.template_name, context)
