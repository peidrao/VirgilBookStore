from django.db.models import Avg, Count
from django.urls import reverse
from django.db import models

from book.choices import BookStatusChoice, CommentStatusChoice
from book.helper import unique_slugify
from user.models import Profile


class Genre(models.Model):
    title = models.CharField(max_length=100, null=False)
    origin = models.ForeignKey(
        "self", related_name="genre_origin", on_delete=models.SET_NULL, null=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("book:book_genre", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title} - {self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "genres"


class Writer(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.FileField(upload_to="images/writer", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("writer_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "writers"


class Book(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to="images/capa", null=True)

    price = models.FloatField()
    amount = models.IntegerField()
    specification = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    is_publish = models.BooleanField(default=False)

    status = models.CharField(choices=BookStatusChoice, default=BookStatusChoice.NEW)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(book=self, status="Verdade").aggregate(
            avarage=Avg("rate")
        )
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(book=self).aggregate(count=Count("id"))
        ctn = 0
        if reviews["count"] is not None:
            ctn = int(reviews["count"])
        return ctn

    class Meta:
        db_table = "books"


class Images(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, blank=True)
    image = models.FileField(blank=True, upload_to="images/books")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book_images"


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)

    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=50, blank=True)
    status = models.CharField(
        choices=CommentStatusChoice, default=CommentStatusChoice.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = "comments"
