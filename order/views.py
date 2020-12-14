from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from .models import ShopCart
from .forms import ShopCartForm


def index(request):
    return HttpResponse('Teste')


@login_required(login_url='/login')
def add_shop_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    check_book = ShopCart.objects.filter(book_id=id)

    if check_book:
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


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for book in shopcart:
        total += book.book.price * book.quantity

    context = {
        'category': category, 'shopcart': shopcart, 'total': total}

    return render(request, 'shopcart_books.html', context)
