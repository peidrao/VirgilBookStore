from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from book.models import Book, Images, Comment
from .models import Comment 
from .forms import CommentForm


def add_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.book_id = id

            data.profile_id = request.user
            data.save()
            messages.success(
                request, 'Sua avaliação foi envianda com sucesso!')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def book_detail(request, id, slug):
    books = Book.objects.all()
    context = {
        'book': books.get(pk=id),
        'images': Images.objects.filter(book_id=id),
        'books': books.filter(genre_id=id),
        'comments': Comment.objects.filter(book_id=id, status='Verdade'),
    }

    return render(request, 'books/book_detail.html', context)


def book_genre(request, slug):
    context = {
        'books': Book.objects.filter(genre__slug=slug)
    }

    return render(request, 'books/book_genre.html', context)
