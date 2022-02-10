from django.core.management.base import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        if not User.objects.filter(email="admin@email.com").exists():
            User.objects.create_superuser("admin", "admin@email.com", "admin")