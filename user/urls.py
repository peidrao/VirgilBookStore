from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='user_index'),
    
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashBoardProfile.as_view(), name='dashboard'),
    path('profile_offers/', views.AddProfileOffersView.as_view(), name='profile_offers'),
    path('profile_newsletter/', views.AddProfileNewsletterView.as_view(), name='profile_newsletter'),
   
    path('update_password/', views.UpdatePasswordView.as_view(), name='update_password'),
    path('update_password_service/', views.UpdatePasswordService.as_view(), name='update_password_service'),
    
    path('update/', views.ProfileUpdateView.as_view(), name='update_profile'),
    
    path('accounts/', views.AccountsListView.as_view(), name='accounts'),
]
