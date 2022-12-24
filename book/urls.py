from django.urls import path

from . import views


app_name = 'book'

urlpatterns = [
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<str:slug>/', views.BookByGenreView.as_view(), name='books_by_genre'),
    path('books/', views.ManagerBoksView.as_view(), name='books'),
]
