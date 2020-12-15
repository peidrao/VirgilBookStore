from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from .models import ShopCart, ShopCartForm

from book.models import Genre


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
        print('1111111111111111111111111111111111111111111111')
        form = ShopCartForm(request.POST)
        print('formulário:  ', form)
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
        print('teste')
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
