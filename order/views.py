from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.contrib import messages
# Create your views here.
from .models import ShopCart, ShopCartForm, Order, OrderBook

from book.models import Genre, Book
from user.models import UserProfile
from .forms import OrderForm


def index(request):
    return HttpResponse('Teste')


@login_required(login_url='/login')
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    checkproduct = ShopCart.objects.filter(book_id=id)
    if checkproduct:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(book_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.book_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
            messages.success(request, "Livro adicionando no carrinho")
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.get(book_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.book_id = id
            data.quantity = 1
            data.save()  #
        messages.success(request, "Livro Adicionado!")
        return HttpResponseRedirect(url)


def shopcart(request):
    genre = Genre.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for book in shopcart:
        total += book.book.price * book.quantity

    context = {
        'genre': genre, 'shopcart': shopcart, 'total': total}

    return render(request, 'shopcart_books.html', context)


@login_required(login_url='/login')
def delete_from_cart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Seu item foi deletado!')
    return HttpResponseRedirect('/shopcart')


@login_required(login_url='/login')
def order_book(request):
    genre = Genre.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    profile = UserProfile.objects.filter(user_id=current_user.id)
    total = 0
    for item in shopcart:
        total += item.book.price * item.quantity
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()
            for rs in shopcart:
                detail = OrderBook()
                detail.order_id = data.id
                detail.book_id = rs.book_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.price
                detail.amount = rs.amount
                detail.save()

                book = Book.objects.get(id=rs.book_id)
                book.amount -= rs.quantity
                book.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(
                request, 'Your order has been completed, Thank You')

            context = {
                'ordercode': ordercode,
                'genre': genre,
            }

            return render(request, 'order_completed.html', context)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/order/orderbook')

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'genre': genre,
               'total': total,
               'form': form,
               'profile': profile}

    return render(request, 'order_form.html', context)
