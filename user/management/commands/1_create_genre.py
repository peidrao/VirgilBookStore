from django.core.management.base import BaseCommand
from book.models import Genre


class Command(BaseCommand):
    """
    Comando para criar gêneros e sub-gêneros de forma estruturada, incluindo descrições.
    """

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Iniciando a criação de gêneros..."))

        genres_structure = [
            ("Arte", None, "Livros sobre diversas formas de arte, como pintura, escultura, música e cinema."),
            ("Comédia", None, "Livros com o objetivo de divertir e provocar o riso."),
            ("Matemática", None, "Livros que exploram conceitos, teorias e a história da matemática."),
            ("Ficção", None, "Obras literárias baseadas na imaginação, não estritamente em fatos."),
            ("Poesia", None, "Textos em verso que exploram a linguagem de forma rítmica e estética."),
            ("Política", None, "Análises e teorias sobre sistemas de governo, poder e comportamento político."),
            ("Religião", None, "Escritos sobre crenças, divindades, rituais e a história das religiões."),
            ("Economia", None, "Estudos sobre a produção, distribuição e consumo de bens e serviços."),
            ("Filosofia", None,
             "Investigação de questões fundamentais sobre existência, conhecimento, valores e razão."),
            ("Filosofia Medieval", "Filosofia", "Filosofia na Europa e no Oriente Médio durante a Idade Média."),
            ("Filosofia Estóica", "Filosofia",
             "Escola filosófica que ensina o desenvolvimento do autocontrole e da fortaleza como meio de superar emoções destrutivas."),
            ("História", None, "Estudo e narração de eventos passados."),
            ("História do Brasil", "História", "Eventos e processos históricos que formaram o Brasil."),
            ("História do Ocidente", "História",
             "História das civilizações ocidentais, desde a antiguidade até a era moderna."),
            ("História Africana", "História", "História dos povos e nações do continente africano."),
        ]

        created_genres = {}

        for title, parent_title, description in genres_structure:
            if title in created_genres:
                continue

            parent_obj = None
            if parent_title:
                if parent_title in created_genres:
                    parent_obj = created_genres[parent_title]
                else:
                    # Garante que o pai exista antes de criar o filho.
                    # A descrição do pai será adicionada quando ele for processado.
                    parent_obj, created = Genre.objects.get_or_create(
                        title=parent_title
                    )
                    created_genres[parent_title] = parent_obj
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f'Gênero "{parent_obj.title}" criado.')
                        )

            # Cria ou obtém o gênero
            genre, created = Genre.objects.get_or_create(
                title=title,
                defaults={"origin": parent_obj, "description": description},
            )
            created_genres[title] = genre

            if created:
                self.stdout.write(self.style.SUCCESS(f'Gênero "{title}" criado com descrição.'))
            else:
                # Se o gênero já existia, verifica se o pai ou a descrição precisam ser atualizados
                needs_save = False
                if genre.origin != parent_obj:
                    genre.origin = parent_obj
                    needs_save = True

                if genre.description != description:
                    genre.description = description
                    needs_save = True

                if needs_save:
                    genre.save()
                    self.stdout.write(
                        self.style.WARNING(
                            f'Gênero "{title}" atualizado.'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Gênero "{title}" já existe e está atualizado.')
                    )

        self.stdout.write(self.style.SUCCESS("Criação de gêneros finalizada."))
