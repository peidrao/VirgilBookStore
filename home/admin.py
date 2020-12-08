from django.contrib import admin

# Register your models here.
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',
                    'updated_at', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']


admin.site.register(ContactMessage, ContactMessageAdmin)
