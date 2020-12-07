from django.shortcuts import render

# Create your views here.
from book.models import Book


def index(request):
    books_latest = Book.objects.all().order_by('-id')[:5]
    context = {
        'books_latest': books_latest
    }
    return render(request, 'index.html', context)
