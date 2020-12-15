from django.contrib import admin

# Register your models here.

from .models import ShopCart, Order, OrderBook


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']


class OrderBookInline(admin.TabularInline):
    model = OrderBook
    readonly_fields = ('user', 'book', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'address', 'city', 'phone',
                       'first_name', 'last_name', 'total')
    can_delete = False
    inlines = [OrderBookInline]


class OrderBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']


admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderBook, OrderBookAdmin)
