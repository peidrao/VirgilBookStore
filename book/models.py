from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Create your models here.

from writer.models import Writer


class Genre(MPTTModel):
    parent = TreeForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(unique=True, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"slug": self.slug})

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Book(models.Model):
    STATUS = (
        ('Sim', 'True'),
        ('Não', 'False'),
    )

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, null=False)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, null=False)

    title = models.CharField(max_length=150, null=False)
    description = RichTextUploadingField()
    keywords = models.CharField(max_length=255)
    publication_date = models.DateField()
    image = models.FileField(upload_to='capa/', null=False)

    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    specification = RichTextUploadingField()
    slug = models.SlugField(unique=True, null=False)

    status = models.CharField(choices=STATUS, max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src={} height="50" />'.format(self.image.url))
        else:
            return ""


class Images(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.FileField(blank=True, upload_to='books/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('Nova', 'Nova'),
        ('Verdade', 'Verdade'),
        ('Falso', 'Falso'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)

    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=50, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default='Nova')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
