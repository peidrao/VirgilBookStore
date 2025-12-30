from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.db.models import Sum
from django.template.loader import render_to_string
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.views import generic

from .choices import ShopCartStatusChoice
from .models import ShopCart, Order, OrderBook

from book.models import Book
from .forms import OrderForm


class ShopCartView(generic.ListView):
    model = ShopCart
    template_name = "pages/orders/cart/index.html"
    context_object_name = "shopcart"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return ShopCart.objects.none()
        return ShopCart.objects.filter(profile=self.request.user, status=ShopCartStatusChoice.IN_CART)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["subtotal"] = self.get_queryset().aggregate(total=Sum("book__price"))["total"] or 0

        return context


class AddToShopCartView(LoginRequiredMixin, View):
    login_url = "/login"

    def post(self, request, id):
        cart_item, created = ShopCart.objects.get_or_create(
            profile=request.user,
            status=ShopCartStatusChoice.IN_CART,
            book_id=id,
            defaults={"quantity": 1},
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        cart_count = ShopCart.objects.filter(profile=request.user, status=ShopCartStatusChoice.IN_CART).count()

        html = render_to_string(
            "partials/cart_badge.html",
            {"cart_count": cart_count},
            request=request,
        )
        return HttpResponse(html)


class RemoveFromShopCartView(LoginRequiredMixin, View):
    login_url = "/login"

    def post(self, request, id):
        ShopCart.objects.filter(id=id, profile=request.user).update(status=ShopCartStatusChoice.REMOVED)

        cart_count = ShopCart.objects.filter(profile=request.user, status=ShopCartStatusChoice.IN_CART).count()

        qs = ShopCart.objects.filter(
            profile=request.user,
            status=ShopCartStatusChoice.IN_CART
        )

        subtotal = qs.aggregate(total=Sum("book__price"))["total"] or 0

        return HttpResponse(
            f"""
            <div id="cart-item-{id}"></div>

            {render_to_string(
                "partials/cart_badge.html",
                {"cart_count": cart_count},
                request=request
            ).replace(
                'id="cart-badge"',
                'id="cart-badge" hx-swap-oob="true"'
            )}
            
             <span id="subtotal" hx-swap-oob="true">
                R$ {subtotal}
            </span>
            """
        )
