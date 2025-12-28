from django.core.management.base import BaseCommand
from book.models import Genre


class Command(BaseCommand):
    """
    Comando para criar categorias de livros de forma estruturada, incluindo descrições.
    """

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Iniciando a criação de categorias de livros..."))

        categories_structure = [
            ("Romance", None, "Narrativas ficcionais centradas em relações humanas e emoções."),
            ("Ficção Científica", None, "Obras que exploram avanços científicos, tecnologia e futuros imaginários."),
            ("Fantasia", None, "Livros com elementos mágicos, mundos imaginários e criaturas fantásticas."),
            ("Mistério", None, "Histórias focadas em crimes, enigmas e investigações."),
            ("Terror", None, "Livros que buscam provocar medo, suspense ou horror."),
            ("Biografia", None, "Relatos sobre a vida de pessoas reais."),
            ("História", None, "Estudos e narrativas sobre eventos históricos."),
            ("Autoajuda", None, "Livros com conselhos para desenvolvimento pessoal e bem-estar."),
            ("Negócios", None, "Temas de administração, economia, empreendedorismo e carreira."),
            ("Infantojuvenil", None, "Livros voltados para crianças e adolescentes."),
            ("Poesia", None, "Textos em verso, explorando linguagem estética e sentimentos."),
            ("Didáticos", None, "Livros para apoio escolar e acadêmico."),
            ("Religião", None, "Obras sobre crenças, espiritualidade e práticas religiosas."),
            ("Filosofia", None, "Reflexões sobre existência, conhecimento, ética e razão."),
            ("HQs e Mangás", None, "Histórias em quadrinhos e mangás japoneses."),
            ("Contos", None, "Narrativas curtas, geralmente com poucos personagens e enredo conciso."),
            ("Drama", None, "Obras que exploram conflitos emocionais e situações intensas."),
            ("Aventura", None, "Livros com enredos dinâmicos, explorações e desafios."),
            ("Literatura Clássica", None, "Obras reconhecidas historicamente por seu valor literário."),
            ("Literatura Nacional", "Literatura", "Livros escritos por autores do país de origem da livraria."),
            ("Literatura Estrangeira", "Literatura", "Livros traduzidos ou escritos por autores de outros países."),
            ("Ensaios", None, "Textos reflexivos sobre temas variados, geralmente de não-ficção."),
            ("Saúde e Bem-estar", None, "Livros sobre cuidados com o corpo, mente e qualidade de vida."),
            ("Gastronomia", None, "Livros de receitas, culinária e cultura alimentar."),
            ("Esportes", None, "Obras sobre práticas esportivas, biografias de atletas e história do esporte."),
            ("Tecnologia", None, "Livros sobre informática, inovação e ciência aplicada."),
            ("Psicologia", None, "Obras sobre comportamento, mente e emoções humanas."),
            ("Educação", None, "Livros sobre métodos de ensino, pedagogia e formação de professores."),
            ("Viagens", None, "Relatos, guias e experiências de viagem."),
            ("Artes", None, "Livros sobre pintura, música, teatro, cinema, fotografia, etc."),
            ("Política", None, "Análises, biografias e discussões sobre sistemas políticos e sociedade."),
            ("Ecologia e Meio Ambiente", None, "Livros sobre natureza, sustentabilidade e preservação ambiental."),
            ("Literatura", None, "Categoria geral para obras literárias de diversos gêneros."),
        ]

        created_categories = {}

        for title, parent_title, description in categories_structure:
            if title in created_categories:
                continue

            parent_obj = None
            if parent_title:
                if parent_title in created_categories:
                    parent_obj = created_categories[parent_title]
                else:
                    parent_obj, created = Genre.objects.get_or_create(
                        title=parent_title
                    )
                    created_categories[parent_title] = parent_obj
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f'Categoria "{parent_obj.title}" criada.')
                        )

            category, created = Genre.objects.get_or_create(
                title=title,
                defaults={"origin": parent_obj, "description": description},
            )
            created_categories[title] = category

            if created:
                self.stdout.write(self.style.SUCCESS(f'Categoria "{title}" criada com descrição.'))
            else:
                needs_save = False
                if category.origin != parent_obj:
                    category.origin = parent_obj
                    needs_save = True
                if category.description != description:
                    category.description = description
                    needs_save = True
                if needs_save:
                    category.save()
                    self.stdout.write(
                        self.style.WARNING(
                            f'Categoria "{title}" atualizada.'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Categoria "{title}" já existe e está atualizada.')
                    )

        self.stdout.write(self.style.SUCCESS("Criação de categorias finalizada."))
