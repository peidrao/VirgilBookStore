from django.urls import path

from . import views


app_name = "market"

urlpatterns = [
    path(
        "wishlist/add/<int:book_id>",
        views.WishListAddService.as_view(),
        name="wishlist_add",
    ),
    path(
        "wishlist/remove/<int:pk>",
        views.WishListRemoveService.as_view(),
        name="wishlist_remove",
    ),
    path("wishlist/", views.WishListView.as_view(), name="wishlist"),
]