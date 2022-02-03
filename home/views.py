import json
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
from book.models import Book, Genre, Images, Comment
from .models import ContactMessage, Banner
from .forms import ContactMessageForm, SearchForm
from order.models import Order, ShopCart


def index(request):
    shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total_books = 0
    for i in shopcart:
        total_books = i.quantity + total_books

    context = {
        'books_latest': Book.objects.all().order_by('-id')[:8],
        'genre': Genre.objects.all(),
        'banner': Banner.objects.all(),
        'order': Order.objects.filter(user_id=request.user.id),
        'total_books': total_books,
    }
    return render(request, 'index.html', context)


def book_detail(request, id, slug):
    context = {
        'genre': Genre.objects.all(),
        'book': Book.objects.get(pk=id),
        'images': Images.objects.filter(book_id=id),
        'books': Book.objects.filter(genre_id=id),
        'comments': Comment.objects.filter(book_id=id, status='Verdade'),
    }

    return render(request, 'pages/book_detail.html', context)


def book_genre(request, id, slug):
    context = {
        'genre': Genre.objects.all(),  
        'books': Book.objects.filter(genre_id=id)
    }
    return render(request, 'pages/book_genre.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')

            data.save()
            return HttpResponseRedirect(reverse('home:contact'))

    context = {
        'form':  ContactMessageForm()
    }

    return render(request, 'pages/contact.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        query = form.cleaned_data['query']
        if form.is_valid():
            context = {
                'query': query,
                'books': Book.objects.filter(title__icontains=query),
                'genre': Genre.objects.all()
            }
            return render(request, 'pages/search_books.html', context)
    return HttpResponseRedirect(reverse('home:index'))


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
