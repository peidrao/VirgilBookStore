from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Profile(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username

    def user_name(self):
        return self.first_name + ' ' + self.last_name + ' [' + self.username + '] '


class ProfileOffer(models.Model):
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)


class ProfileNewsletter(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
