from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=300, blank=True)

    status = models.CharField(max_length=6, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    note = models.CharField(max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
