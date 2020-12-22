import admin_thumbnails
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from .models import Genre, Book, Images, Comment


class GenreAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_books_count', 'related_books_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Genre.objects.add_related_count(
            qs, Book, 'genre', 'books_cumulative_count', cumulative=True)

        qs = Genre.objects.add_related_count(
            qs, Book, 'genre', 'books_count', cumulative=False)

        return qs

    def related_books_count(self, instance):
        return instance.books_count
    related_books_count.short_description = 'Livros desta categoria específica'

    def related_books_cumulative_count(self, instance):
        return instance.books_cumulative_count
    related_books_cumulative_count.short_description = 'Livros relacionados'


@admin_thumbnails.thumbnail('image')
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


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'image_thumbnail']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'created_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'user', 'book')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)
