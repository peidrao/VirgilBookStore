from django.utils.safestring import mark_safe
from django.db import models


class ContactMessage(models.Model):
    STATUS = (
        ("New", "New"),
        ("Read", "Read"),
        ("Closed", "Closed"),
    )

    name = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=300, blank=True)

    status = models.CharField(max_length=6, choices=STATUS, default="New")
    ip = models.CharField(max_length=20, blank=True)
    note = models.CharField(max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=False)
    image = models.FileField(upload_to="images/banner", null=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src={} height="50"  />'.format(self.image.url))
        else:
            return ""
