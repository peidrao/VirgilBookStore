from django.urls import path

from . import views


app_name = 'book'

urlpatterns = [
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
