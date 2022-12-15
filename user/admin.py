from django.contrib import admin

# Register your models here.

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'phone', 'city']


admin.site.register(Profile, ProfileAdmin)
