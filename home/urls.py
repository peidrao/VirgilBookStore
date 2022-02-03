from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('book/<int:id>/<slug:slug>', views.book_detail, name='book_detail'),
    path('genre/<int:id>/<slug:slug>',
         views.book_genre, name='book_genre'),
    path('contact/', views.contact, name='contact'),
]
