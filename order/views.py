from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import ShopCart


def index(request):
    return HttpResponse('Teste')


@login_required(login_url='/login')
def add_shop_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    check_product = ShopCart.objects.filter(product_id=id)

    if check_product:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form  = ShopCart(request.POST)
        if form.i
