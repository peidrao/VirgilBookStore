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


def shopcart(request):
    shopcart = ShopCart.objects.filter(profile=request.user)
    total = 0
    for book in shopcart:
        total = book.book.price * book.quantity

    context = {"shopcart": shopcart, "total": total}

    return render(request, "order/shopcart_books.html", context)


@login_required(login_url="/login")
def delete_from_cart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Seu item foi deletado!")
    return HttpResponseRedirect("/shopcart")


@login_required(login_url="/login")
def order_book(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(profile=current_user)
    total = 0
    for item in shopcart:
        total += item.book.price * item.quantity
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data["first_name"]
            data.last_name = form.cleaned_data["last_name"]
            data.address = form.cleaned_data["address"]
            data.city = form.cleaned_data["city"]
            data.phone = form.cleaned_data["phone"]
            data.profile = current_user.id
            data.total = total
            data.ip = request.META.get("REMOTE_ADDR")
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()
            for rs in shopcart:
                detail = OrderBook()
                detail.order_id = data.id
                detail.book_id = rs.book_id
                detail.profile_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.price
                detail.amount = rs.amount
                detail.save()

                book = Book.objects.get(id=rs.book_id)
                book.amount -= rs.quantity
                book.save()

            ShopCart.objects.filter(profile_id=current_user.id).delete()
            request.session["cart_items"] = 0
            messages.success(request, "Your order has been completed, Thank You")

            context = {
                "ordercode": ordercode,
            }

            return render(request, "order_completed.html", context)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderbook")

    form = OrderForm()
    context = {
        "shopcart": shopcart,
        "total": total,
        "form": form,
        "profile": current_user,
    }

    return render(request, "order/order_form.html", context)
