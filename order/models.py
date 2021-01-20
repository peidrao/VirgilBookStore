from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

# Create your models here.
from book.models import Book


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.book.title

    @property
    def price(self):
        return (self.book.price)

    @property
    def amount(self):
        return (self.quantity * self.book.price)
    
    @property
    def quantity_books(self):
        return self.quantity



class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']

class Order(models.Model):
    STATUS = (
        ('Novo', 'Novo'),
        ('Aceitaram', 'Aceitaram'),
        ('Prepararam', 'Prepararam'),
        ('Enviaram', 'Enviaram'),
        ('Concluído', 'Concluído'),
        ('Cancelaram', 'Cancelaram'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)

    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=10, null=False)

    phone = models.CharField(blank=True, max_length=11)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(max_length=100)

    total = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=10, default='Novo')

    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    usernote = models.CharField(blank=True, max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderBook(models.Model):
    STATUS = (
        ('Novo', 'Novo'),
        ('Aceitaram', 'Aceitaram'),
        ('Cancelaram', 'Cancelaram'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()

    status = models.CharField(choices=STATUS, max_length=10, default='Novo')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title
