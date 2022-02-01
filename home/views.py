from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import json

# Create your views here.
from book.models import Book, Genre, Images, Comment
from .models import ContactMessage, Banner
from .forms import ContactMessageForm, SearchForm
from order.models import Order, ShopCart


def index(request):
    banner = Banner.objects.all()
    genre = Genre.objects.all()
    books_latest = Book.objects.all().order_by('-id')[:8]
    current_user = request.user
    order = Order.objects.filter(user_id=current_user.id)
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total_books = 0
    for i in shopcart:
        total_books = i.quantity + total_books

    context = {
        'books_latest': books_latest,
        'genre': genre,
        'banner': banner,
        'order': order,
        'total_books': total_books,
    }
    return render(request, 'index.html', context)


def book_detail(request, id, slug):
    genre = Genre.objects.all()
    book = Book.objects.get(pk=id)
    books = Book.objects.filter(genre_id=id)
    comments = Comment.objects.filter(book_id=id, status='Verdade')

    images = Images.objects.filter(book_id=id)
    context = {
        'genre': genre,
        'book': book,
        'images': images,
        'books': books,
        'comments': comments,
    }

    return render(request, 'pages/book_detail.html', context)


def book_genre(request, id, slug):
    # query = request.GET.get('q')
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


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            genre = Genre.objects.all()

            context = {
                'query': query,
                'books': books,
                'genre': genre,
            }
            return render(request, 'pages/search_books.html', context)
    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        books = Book.objects.filter(title__icontains=q)
        results = []
        for item in books:
            results.append(item.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
