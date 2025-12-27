from django.contrib import admin

# Register your models here.
from .models import ContactMessage, Banner


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "updated_at", "status"]
    readonly_fields = ("name", "subject", "email", "message", "ip")
    list_filter = ["status"]


class BannerAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "image_tag"]
    readonly_fields = ("image_tag",)


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Banner, BannerAdmin)
