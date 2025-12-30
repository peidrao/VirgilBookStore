from django.db import models
from django.forms import ModelForm

from order.choices import ShopCartStatusChoice
from user.models import Profile

from book.models import Book


class ShopCart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=30, choices=ShopCartStatusChoice.choices, default=ShopCartStatusChoice.IN_CART)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = "shop_carts"

    def __str__(self):
        return self.book.title


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ["quantity"]


class Order(models.Model):
    STATUS = (
        ("Novo", "Novo"),
        ("Aceitaram", "Aceitaram"),
        ("Prepararam", "Prepararam"),
        ("Enviaram", "Enviaram"),
        ("Concluído", "Concluído"),
        ("Cancelaram", "Cancelaram"),
    )

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)

    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=10, null=False)

    phone = models.CharField(blank=True, max_length=11)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(max_length=100)

    total = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=10, default="Novo")

    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    usernote = models.CharField(blank=True, max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.first_name

    class Meta:
        db_table = "orders"


class OrderBook(models.Model):
    STATUS = (
        ("Novo", "Novo"),
        ("Aceitaram", "Aceitaram"),
        ("Cancelaram", "Cancelaram"),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()

    status = models.CharField(choices=STATUS, max_length=10, default="Novo")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title

    class Meta:
        db_table = "order_books"