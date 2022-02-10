from django.core.management.base import BaseCommand

from book.models import Genre


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Genre.objects.filter(slug="arte").exists():
            Genre.objects.create(title="Arte")
        if not Genre.objects.filter(slug="acao").exists():
            Genre.objects.create(title="Ação")
        if not Genre.objects.filter(slug="comedia").exists():
            Genre.objects.create(title="Comédia")
        if not Genre.objects.filter(slug="ficcao").exists():
            Genre.objects.create(title="Ficção")
        if not Genre.objects.filter(slug="contos-de-fada").exists():
            Genre.objects.create(title="Contos de Fada")
        if not Genre.objects.filter(slug="poesia").exists():
            Genre.objects.create(title="Poesia")
        if not Genre.objects.filter(slug="politica").exists():
            Genre.objects.create(title="Política")
        if not Genre.objects.filter(slug="religiao").exists():
            Genre.objects.create(title="Religião")
        if not Genre.objects.filter(slug="economia").exists():
            Genre.objects.create(title="Econômia")
        if not Genre.objects.filter(slug="filosofia").exists():
            Genre.objects.create(title="Filosofia")