from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("addtoshopcart/<int:id>", views.addtoshopcart, name="addtoshopcart"),
    path("deletefromcart/<int:id>", views.delete_from_cart, name="delete_from_cart"),
    path("orderbook/", views.order_book, name="order_book"),
]
