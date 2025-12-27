from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from book.helpers import create_book_payload
from book.models import Book, Images, Comment, Genre
from django.shortcuts import get_object_or_404

from .forms import CommentForm
from django.views import generic
from rest_framework import generics, status, permissions, views
from rest_framework.response import Response

from virgilbookstore.permissions import AdministratorPermission


class BookDetailView(generic.DetailView):
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs["pk"])
        context = {"book": book}
        return render(request, "books/book_detail.html", context)


class BookByGenreView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        genre = get_object_or_404(Genre, slug=kwargs["slug"])

        books = Book.objects.filter(genre=genre)
        context = {"books": books, "genre": genre}
        return render(request, "books/book_genre.html", context=context)


class ManagerBoksView(AdministratorPermission, generic.ListView):
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        books = Book.objects.all().order_by("created_at")
        context = {"books": books}
        return render(request, "books/books.html", context=context)


class ManagerBookAddView(generic.TemplateView):
    template_name = "books/book_add.html"


class ManagerBookUpdateView(generic.TemplateView):
    template_name = "books/book_update.html"
    queryset = Book.objects.all()

    def get(self, request, pk):
        book = self.queryset.get(pk=pk)
        return render(request, self.template_name, {"book": book})


class ManageRemoveBook(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class ManagerBookExportService(views.APIView):
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        books = self.queryset.all().values("id", "title")

        return Response(books, status=status.HTTP_200_OK)


class ManagerBookUpdateService(generics.UpdateAPIView):
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        book = self.get_object()
        payload = create_book_payload(request)
        if book:
            self.queryset.filter(id=book.id).update(**payload)
            return Response(
                {"message": "Successfully updated book"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "There was an error in the update"},
            status=status.HTTP_400_BAD_REQUEST,
        )


def add_comment(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data["subject"]
            data.comment = form.cleaned_data["comment"]
            data.rate = form.cleaned_data["rate"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.book_id = id

            data.profile_id = request.user
            data.save()
            messages.success(request, "Sua avaliação foi envianda com sucesso!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def book_detail(request, id, slug):
    books = Book.objects.all()
    context = {
        "book": books.get(pk=id),
        "images": Images.objects.filter(book_id=id),
        "books": books.filter(genre_id=id),
        "comments": Comment.objects.filter(book_id=id, status="Verdade"),
    }

    return render(request, "books/book_detail.html", context)


def book_genre(request, slug):
    context = {"books": Book.objects.filter(genre__slug=slug)}

    return render(request, "books/book_genre.html", context)
