import json

from django.shortcuts import render
from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views import generic

from market.models import Cart, CartItem, Coupon, WishList
from book.models import Book
from market.serializers import CouponSerializer


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


class CartDetailsService(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = (IsAuthenticated,)

    def update(self, request, pk, *args, **kwargs):
        action = request.data.get("action")

        cart_item = self.queryset.get(id=pk)
        if action == "plus":
            cart_item.amount += 1
        if action == "minus":
            cart_item.amount -= 1
            if cart_item.amount == 0:
                cart_item.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        cart_item.price = cart_item.book.price * cart_item.amount
        cart_item.save()

        cart = cart_item.cart
        total = cart.cart_item.aggregate(total=Sum("price"))["total"]
        cart.total = total
        cart.save()

        response = {"price": cart_item.price, "total": cart.total}
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart = Cart.objects.get(profile=request.user)

        cart.total -= cart_item.price
        cart.save()
        cart_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CouponsListView(generic.ListView):
    template_name = "pages/coupons.html"
    queryset = Coupon.objects.all().order_by("created_at")


class CouponsUpdateView(generic.DetailView):
    template_name = "market/coupons_update.html"
    queryset = Coupon.objects.all()


class CouponsAddView(generic.TemplateView):
    template_name = "market/coupons_add.html"


class CouponUpdateStatusService(generics.UpdateAPIView):
    queryset = Coupon.objects.all()
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        coupon = self.get_object()
        is_active = request.data.get("checked")

        if is_active == "false":
            is_active = False
        else:
            is_active = True

        coupon.is_active = is_active
        coupon.save()
        return Response(
            {"message": "Coupon updated successfully"}, status=status.HTTP_200_OK
        )


class CouponDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        data = request.body.decode("UTF-8")
        data = json.loads(data)
        coupon = self.get_object()
        coupon.name = data.get("name")
        coupon.discount = int(data.get("discount"))
        coupon.save()
        return Response(
            {"message": "Coupon updated successfully"}, status=status.HTTP_200_OK
        )


class CouponsAddService(generics.CreateAPIView):
    queryset = Coupon.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CouponSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CouponApplyService(generics.CreateAPIView):
    queryset = Coupon.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        coupon = request.data.get("coupon")
        if not self.queryset.filter(name=coupon, is_active=True).exists():
            return Response(
                {"message": "Invalid coupon"}, status=status.HTTP_400_BAD_REQUEST
            )

        coupon = self.queryset.get(name=coupon)

        cart = Cart.objects.get(profile=request.user)
        total_discount = cart.total * (coupon.discount / 100)
        cart.discount = total_discount
        cart.total_discount = cart.total - total_discount
        cart.save()

        context = {"discount": total_discount, "total_price": cart.total_discount}
        return Response(context, status=status.HTTP_200_OK)
