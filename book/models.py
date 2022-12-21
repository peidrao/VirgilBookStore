
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models import Avg, Count
from django.urls import reverse
from django.db import models
from user.models import Profile
from django.utils.translation import gettext as _


def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)

class Genre(models.Model):
    title = models.CharField(max_length=100, null=False)
    origin = models.ForeignKey('self', related_name='genre_origin', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('book:book_genre', kwargs={"slug": self.slug})
        
    def __str__(self):
        full_path = [self.title]
        k = self.origin
        while k is not None:
            full_path.append(k.title)
            k = k.origin
        return ' / '.join(full_path[::-1])


class Writer(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.FileField(upload_to='images/writer', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("writer_detail", kwargs={"slug": self.slug})


class Book(models.Model):
    class StatusChoice(models.IntegerChoices):
        YES = 1, _('Yes')
        NOT = 2, _('Not')

    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='images/capa', null=True)

    price = models.FloatField()
    amount = models.IntegerField()
    specification = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)

    status = models.IntegerField(choices=StatusChoice.choices, default=StatusChoice.YES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(
            book=self, status='Verdade').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews['avarage'] is not None:
            avg = float(reviews['avarage'])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(
            book=self).aggregate(count=Count('id'))
        cnt = 0
        if reviews['count'] is not None:
            ctn = int(reviews['count'])
        return ctn


class Images(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, blank=True)
    image = models.FileField(blank=True, upload_to='images/books')

    def __str__(self):
        return self.title


class Comment(models.Model):
    class StatusChoice(models.IntegerChoices):
        NEW = 1, _('New')
        READ = 2, _('Read')
        TRASH = 3, _('Trash')

    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)

    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=50, blank=True)
    status = models.IntegerField(choices=StatusChoice.choices, default=StatusChoice.NEW)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


pre_save.connect(slugify_pre_save, sender=Genre)