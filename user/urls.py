from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='user_index'),
    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment,
         name='user_deletecomment'),
    path('orders/', views.user_orders, name='user_orders'),
    path('request/', views.user_request, name='user_request'),
    path('order_book/', views.user_order_book, name='user_order_book'),
     path('signup/', views.signup_form, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.index, name='profile'),
    path('logout/', views.logout, name='logout')
]
