from django.core.management.base import BaseCommand

from book.models import Genre


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Genre.objects.filter(slug="arte").exists():
            Genre.objects.create(title="Arte")
        if not Genre.objects.filter(slug="comedia").exists():
            Genre.objects.create(title="Comédia")
        if not Genre.objects.filter(slug="matematica").exists():   
            Genre.objects.create(title="Matemática")
        if not Genre.objects.filter(slug="ficcao").exists():
            Genre.objects.create(title="Ficção")
        if not Genre.objects.filter(slug="poesia").exists():
            Genre.objects.create(title="Poesia")
        if not Genre.objects.filter(slug="politica").exists():
            Genre.objects.create(title="Política")
        if not Genre.objects.filter(slug="religiao").exists():
            Genre.objects.create(title="Religião")
        if not Genre.objects.filter(slug="economia").exists():
            Genre.objects.create(title="Econômia")
        if not Genre.objects.filter(slug="filosofia").exists():
            philosophy = Genre.objects.create(title="Filosofia")
            if not Genre.objects.filter(slug='filosofia-medieval').exists():
                Genre.objects.create(title="Filosofia Medieval", origin=philosophy)
            if not Genre.objects.filter(slug='filosofia-estoica').exists():
                Genre.objects.create(title="Filosofia Estóica", origin=philosophy)
        if not Genre.objects.filter(slug='historia').exists():
            history = Genre.objects.create(title="História")
            if not Genre.objects.filter(slug='historia-do-brasil').exists():
                Genre.objects.create(title="História do Brasil", origin=history)
            if not Genre.objects.filter(slug='historia-do-0ocidente').exists():
                Genre.objects.create(title="História do Ocidente", origin=history)
            if not Genre.objects.filter(slug='historia-africana').exists():
                Genre.objects.create(title="História Africana", origin=history)
            
