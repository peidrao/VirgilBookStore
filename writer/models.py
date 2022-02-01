from django.utils.safestring import mark_safe
from django.urls import reverse

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Writer(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    description = RichTextUploadingField()
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
