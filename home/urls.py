from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    # path('', views.index, name='index'),
    # path('search/', views.search, name='search'),
    # path('search_auto/', views.search_auto, name='search_auto'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path("", views.HomeView.as_view(), name="home"),
]
