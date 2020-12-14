from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', views.add_shop_cart, name='add_shop_cart'),
]
