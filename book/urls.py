from django.urls import path

from . import views


app_name = 'book'

urlpatterns = [
    path('addcomment/<int:id>', views.add_comment, name='add_comment'),
    path('book/<int:id>/<slug:slug>', views.book_detail, name='book_detail'),
    path('genre/<slug:slug>', views.book_genre, name='book_genre'),
]
