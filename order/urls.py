from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>',
         views.delete_from_cart, name='delete_from_cart'),
    path('orderbook/',
         views.order_book, name='order_book'),
]
