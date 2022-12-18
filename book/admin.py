from django.contrib import admin

from .models import Book, Genre, Images, Comment, Writer


class WriterAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'created_at']
    prepopulated_fields = {'slug': ('fullname',)}
    search_fields = ['fullname']
    ordering  = ['fullname']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'status']
    list_filter = ['genre']
    prepopulated_fields = {'slug': ('title',)}

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',]



class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'created_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'profile', 'book')


admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Genre, GenreAdmin)