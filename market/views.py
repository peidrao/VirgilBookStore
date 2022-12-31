from requests import delete
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.views import generic

from market.models import WishList


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
