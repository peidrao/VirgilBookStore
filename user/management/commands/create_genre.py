from django.core.management.base import BaseCommand
from book.models import Genre


class Command(BaseCommand):
    """
    Comando para criar gêneros e sub-gêneros de forma estruturada.
    """
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Iniciando a criação de gêneros..."))

        genres_structure = [
            ("Arte", None),
            ("Comédia", None),
            ("Matemática", None),
            ("Ficção", None),
            ("Poesia", None),
            ("Política", None),
            ("Religião", None),
            ("Economia", None), # Corrigido de "Econômia"
            ("Filosofia", None),
            ("Filosofia Medieval", "Filosofia"),
            ("Filosofia Estóica", "Filosofia"),
            ("História", None),
            ("História do Brasil", "História"),
            ("História do Ocidente", "História"),
            ("História Africana", "História"),
        ]

        created_genres = {}

        for title, parent_title in genres_structure:
            # Verifica se o gênero já foi processado nesta execução
            if title in created_genres:
                continue

            parent_obj = None
            if parent_title:
                # Busca o objeto do pai, que já deve ter sido criado
                if parent_title in created_genres:
                    parent_obj = created_genres[parent_title]
                else:
                    # Garante que o pai exista antes de criar o filho
                    parent_obj, created = Genre.objects.get_or_create(title=parent_title)
                    created_genres[parent_title] = parent_obj
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Gênero "{parent_obj.title}" criado.'))

            # Cria ou obtém o gênero, associando ao pai se houver
            genre, created = Genre.objects.get_or_create(
                title=title,
                defaults={'origin': parent_obj}
            )
            created_genres[title] = genre

            if created:
                self.stdout.write(self.style.SUCCESS(f'Gênero "{title}" criado.'))
            else:
                # Se o gênero já existia, mas o pai mudou, atualiza
                if genre.origin != parent_obj:
                    genre.origin = parent_obj
                    genre.save()
                    self.stdout.write(self.style.WARNING(f'Gênero "{title}" atualizado com o pai "{parent_title}".'))
                else:
                    self.stdout.write(self.style.WARNING(f'Gênero "{title}" já existe.'))

        self.stdout.write(self.style.SUCCESS("Criação de gêneros finalizada."))
