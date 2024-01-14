from django.core.management.base import BaseCommand

from user.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):

        if not Profile.objects.filter(email="admin@email.com").exists():
            Profile.objects.create_superuser("admin", "admin@email.com", "admin")
