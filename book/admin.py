from django.contrib import admin

from .models import Book, Images, Comment, Writer


class WriterAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'created_at', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('fullname',)}
    search_fields = ['fullname']
    ordering  = ['fullname']


class BookImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'status', 'image_tag']
    list_filter = ['genre']
    readonly_fields = ('image_tag',)
    inlines = [BookImageInline]
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title',]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'created_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'profile', 'book')


admin.site.register(Book, BookAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Writer, WriterAdmin)