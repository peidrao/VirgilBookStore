from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from book.models import Book, Genre, Images
from .models import ContactMessage, Banner
from .forms import ContactMessageForm


def index(request):
    banner = Banner.objects.all()
    genre = Genre.objects.all()
    books_latest = Book.objects.all().order_by('-id')[:8]
    context = {
        'books_latest': books_latest,
        'genre': genre,
        'banner': banner,
    }

    return render(request, 'index.html', context)


def book_detail(request, id, slug):
    query = request.GET.get('q')
    genre = Genre.objects.all()
    book = Book.objects.get(pk=id)
    books = Book.objects.filter(genre_id=id)

    images = Images.objects.filter(book_id=id)
    context = {
        'genre': genre,
        'book': book,
        'images': images,
        'books': books,
    }

    return render(request, 'pages/book_detail.html', context)


def book_genre(request, id, slug):
    #query = request.GET.get('q')
    genre = Genre.objects.all()
    books = Book.objects.filter(genre_id=id)

    context = {
        'genre': genre,  'books': books}
    return render(request, 'pages/book_genre.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']  # Get from input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')

            data.save()
            return HttpResponseRedirect('/contact')

    form = ContactMessageForm
    context = {
        'form': form
    }

    return render(request, 'pages/contact.html', context)
