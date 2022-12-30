from django.urls import path

from . import views


app_name = "book"

urlpatterns = [
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("book/<str:slug>/", views.BookByGenreView.as_view(), name="books_by_genre"),
    path("books/", views.ManagerBoksView.as_view(), name="books"),
    path("book/remove/<int:pk>", views.ManageRemoveBook.as_view(), name="remove"),
    path("add/", views.ManagerBookAddView.as_view(), name="book_add"),
    path(
        "book/update/<int:pk>",
        views.ManagerBookUpdateView.as_view(),
        name="book_update",
    ),
    path("book/create", views.ManagerBookAddService.as_view(), name="book_create"),
    path("book/export", views.ManagerBookExportService.as_view(), name="book_export"),
]
