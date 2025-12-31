from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.db.models import Sum
from django.template.loader import render_to_string
from django.views import generic

from .choices import ShopCartStatusChoice
from .models import ShopCart

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
        ShopCart.objects.filter(
            id=id,
            profile=request.user
        ).update(status=ShopCartStatusChoice.REMOVED)

        qs = ShopCart.objects.filter(
            profile=request.user,
            status=ShopCartStatusChoice.IN_CART
        )

        cart_count = qs.count()

        badge_html = render_to_string(
            "partials/cart_badge.html",
            {"cart_count": cart_count},
            request=request
        ).replace('id="cart-badge"', 'id="cart-badge" hx-swap-oob="true"')

        remove_item_html = f'<div id="cart-item-{id}"></div>'

        if cart_count == 0:
            empty_items = render_to_string(
                "pages/orders/cart/partials/_cart_empty.html",
                request=request
            )
            empty_summary = render_to_string(
                "pages/orders/cart/partials/_cart_summary_empty.html",
                request=request
            )

            cart_items_oob = f"""
            <div id="cart-items" class="lg:col-span-2 space-y-4" hx-swap-oob="true">
                {empty_items}
            </div>
            """

            cart_summary_oob = f"""
            <div id="cart-summary" class="lg:col-span-1" hx-swap-oob="true">
                {empty_summary}
            </div>
            """

            return HttpResponse("\n".join([remove_item_html, badge_html, cart_items_oob, cart_summary_oob]))

        return HttpResponse("\n".join([remove_item_html, badge_html]))
