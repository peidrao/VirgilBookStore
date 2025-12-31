from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("shopcart/", views.ShopCartView.as_view(), name="shopcart"),
    path("addtoshopcart/<int:id>", views.AddToShopCartView.as_view(), name="addtoshopcart"),
    path('removefromshopcart/<int:id>', views.RemoveFromShopCartView.as_view(), name='removefromshopcart'),

    path('checkout/', views.CheckoutView.as_view(), name='checkout')
]
