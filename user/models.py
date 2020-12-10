
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=150, blank=True)
    number_address = models.IntegerField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    image = models.FileField(upload_to='user/', blank=True)

    def __str__(self):
        return self.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
