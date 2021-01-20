from django.contrib import admin

# Register your models here.
from .models import Writer


class WriterAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'created_at', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('fullname',)}
    search_fields = ['fullname']
    ordering  = ['fullname']


admin.site.register(Writer, WriterAdmin)
