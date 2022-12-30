from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("", views.index, name="user_index"),
    path("login/", views.login, name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.DashBoardProfile.as_view(), name="dashboard"),
    path(
        "profile_offers/", views.AddProfileOffersView.as_view(), name="profile_offers"
    ),
    path(
        "profile_newsletter/",
        views.AddProfileNewsletterView.as_view(),
        name="profile_newsletter",
    ),
    path(
        "update_password/", views.UpdatePasswordView.as_view(), name="update_password"
    ),
    path(
        "update_password_service/",
        views.UpdatePasswordService.as_view(),
        name="update_password_service",
    ),
    path("update/", views.ProfileUpdateView.as_view(), name="update_profile"),
    path(
        "profile_update/<int:pk>",
        views.ProfileUpdateService.as_view(),
        name="update_profile_service",
    ),
    path(
        "profile/remove/<int:pk>",
        views.ProfileRemoveService.as_view(),
        name="remove_profile_service",
    ),
    path("accounts/", views.AccountsListView.as_view(), name="accounts"),
    path("banners/", views.ManagerBannersView.as_view(), name="banners"),
]
