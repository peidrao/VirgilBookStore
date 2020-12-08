from django.shortcuts import render

# Create your views here.
from book.models import Book, Genre, Images


def index(request):
    books_latest = Book.objects.all().order_by('-id')[:8]
    context = {
        'books_latest': books_latest
    }
    return render(request, 'index.html', context)


def book_detail(request, id, slug):
    query = request.GET.get('q')
    genre = Genre.objects.all()
    book = Book.objects.get(pk=id)

    images = Images.objects.filter(book_id=id)
    context = {
        'genre': genre,
        'book': book,
        'images': images,
    }

    return render(request, 'pages/book_detail.html', context)
