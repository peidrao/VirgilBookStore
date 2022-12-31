from django.db import models
from django.utils import timezone

from book.models import Book
from user.models import Profile


class WishList(models.Model):
    book = models.ForeignKey(
        Book, related_name="wishlist_book", on_delete=models.SET_NULL, null=True
    )
    profile = models.ForeignKey(
        Profile, related_name="wishlist_profile", on_delete=models.SET_NULL, null=True
    )

    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
