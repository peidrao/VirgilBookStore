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
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/add/", views.CartAddService.as_view(), name="cart_add"),
    path("cart/<int:pk>", views.CartDetailsService.as_view(), name="cart_add"),
    path("coupons/add/", views.CouponsAddView.as_view(), name="coupon_add"),
    path(
        "coupons/add/service",
        views.CouponsAddService.as_view(),
        name="coupon_add_service",
    ),
    path("coupons/", views.CouponsListView.as_view(), name="coupon"),
    path(
        "coupons/<int:pk>/update/status",
        views.CouponUpdateStatusService.as_view(),
        name="coupon_update_status",
    ),
    path(
        "coupons/<int:pk>/update",
        views.CouponsUpdateView.as_view(),
        name="coupon_update",
    ),
    path(
        "coupons/<int:pk>",
        views.CouponDetails.as_view(),
        name="coupon_details",
    ),
]
