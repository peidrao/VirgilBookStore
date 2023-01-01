from django.db import models
from django.utils import timezone

from book.models import Book
from user.models import Profile


class WishList(models.Model):
    book = models.ForeignKey(
        Book, related_name="wishlist_book", on_delete=models.SET_NULL, null=True
    )
    profile = models.ForeignKey(
        Profile, related_name="wishlist_profile", on_delete=models.SET_NULL, null=True
    )

    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)


class Cart(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="cart_profile", on_delete=models.SET_NULL, null=True
    )
    total = models.FloatField(default=0)


class CartItem(models.Model):
    book = models.ForeignKey(
        Book, related_name="cart_item_book", on_delete=models.SET_NULL, null=True
    )
    profile = models.ForeignKey(
        Profile, related_name="cart_item_profile", on_delete=models.SET_NULL, null=True
    )
    amount = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    cart = models.ForeignKey(
        Cart, related_name="cart_item", on_delete=models.SET_NULL, null=True
    )

    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)


class Coupon(models.Model):
    value = models.CharField(max_length=18)
    discount = models.IntegerField()
    is_active = models.BooleanField(null=True)
    created_at = models.BooleanField(null=True)

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
