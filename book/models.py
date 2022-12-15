from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models import Avg, Count
from django.urls import reverse
from django.db import models
from user.models import Profile


def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)

class Genre(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('book:book_genre', kwargs={"slug": self.slug})
        
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Writer(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=False, blank=True)
    image = models.FileField(upload_to='images/writer', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src={} height="50"  />'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse("writer_detail", kwargs={"slug": self.slug})


class Book(models.Model):
    STATUS = (
        ('Sim', 'True'),
        ('Não', 'False'),
    )

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, null=False)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, null=False)

    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to='images/capa', null=False)

    price = models.FloatField()
    amount = models.IntegerField()
    specification = models.TextField(null=True, blank=True)
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
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.FileField(blank=True, upload_to='images/books')

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('Nova', 'Nova'),
        ('Verdade', 'Verdade'),
        ('Falso', 'Falso'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)

    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=50, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default='Nova')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


pre_save.connect(slugify_pre_save, sender=Genre)