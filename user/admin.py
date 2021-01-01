from django.contrib import admin

# Register your models here.

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'phone', 'city']


admin.site.register(UserProfile, UserProfileAdmin)
