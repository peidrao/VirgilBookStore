import json
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from book.models import Book
from .models import ContactMessage, Banner
from .forms import ContactMessageForm, SearchForm
from order.models import Order, ShopCart


def index(request):
    shopcart = ShopCart.objects.filter(profile=request.user)
    total_books = 0
    for i in shopcart:
        total_books = i.quantity + total_books
    context = {
        'books_latest': Book.objects.all().order_by('-id')[:8],
        'banner': Banner.objects.all(),
        'order': Order.objects.filter(profile_id=request.user.id),
        'total_books': total_books,
    }
    return render(request, 'index.html', context)


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
