from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment,
         name='user_deletecomment'),
    path('orders/', views.user_orders, name='user_orders'),
    path('request/', views.user_request, name='user_request')
]
