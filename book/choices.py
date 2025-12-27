from django.db import models


class BookStatusChoice(models.TextChoices):
    NEW = "NEW", "new"
    DISCOUNTED = "DISCOUNTED", "discounted"
    REGULAR = "REGULAR", "regular"
    SOLD_OUT = "SOLD_OUT", "sold_out"
    ARCHIVED = "ARCHIVED", "archived"
    PREORDER = "PREORDER", "preorder"


class CommentStatusChoice(models.TextChoices):
    PENDING = "PENDING", "pending"
    APPROVED = "APPROVED", "approved"
    REJECTED = "REJECTED", "rejected"
