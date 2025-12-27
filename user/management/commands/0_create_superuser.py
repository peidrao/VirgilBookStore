from django.core.management.base import BaseCommand

from user.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Profile.objects.filter(is_superuser=True).exists():
            profile = Profile.objects.create(
                username="peidrao",
                email="peidrao@gmail.com",
                is_superuser=True,
                is_staff=True,
                first_name="Pedro",
                last_name="Fonseca",
            )
            profile.set_password("123")
            profile.save()
        self.stdout.write(self.style.SUCCESS("Superuser criado!"))
