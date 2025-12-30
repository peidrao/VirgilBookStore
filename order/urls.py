from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("shopcart/", views.ShopCartView.as_view(), name="shopcart"),

    path("addtoshopcart/<int:id>", views.AddToShopCartView.as_view(), name="addtoshopcart"),
    path("deletefromcart/<int:id>", views.delete_from_cart, name="delete_from_cart"),
    path("orderbook/", views.order_book, name="order_book"),
]
