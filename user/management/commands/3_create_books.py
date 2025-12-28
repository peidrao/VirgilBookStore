from decimal import Decimal
from django.core.management.base import BaseCommand
from book.models import Book, Genre, Writer


books = [
    {"title": "O Senhor dos Anéis: A Sociedade do Anel", "description": "Primeiro volume da trilogia épica de fantasia.", "author": "J. R. R. Tolkien", "genre": "Fantasia", "price": 89.90, "amount": 10},
    {"title": "O Senhor dos Anéis: As Duas Torres", "description": "Segundo volume da trilogia épica de fantasia.", "author": "J. R. R. Tolkien", "genre": "Fantasia", "price": 89.90, "amount": 10},
    {"title": "O Senhor dos Anéis: O Retorno do Rei", "description": "Terceiro volume da trilogia épica de fantasia.", "author": "J. R. R. Tolkien", "genre": "Fantasia", "price": 89.90, "amount": 10},
    {"title": "O Hobbit", "description": "A aventura de Bilbo Bolseiro antes da trilogia O Senhor dos Anéis.", "author": "J. R. R. Tolkien", "genre": "Fantasia", "price": 59.90, "amount": 12},
    {"title": "Silmarillion", "description": "Histórias da Primeira Era da Terra Média.", "author": "J. R. R. Tolkien", "genre": "Fantasia", "price": 69.90, "amount": 8},
    {"title": "Harry Potter e a Pedra Filosofal", "description": "Primeiro livro da saga Harry Potter.", "author": "J. K. Rowling", "genre": "Fantasia", "price": 49.90, "amount": 15},
    {"title": "Harry Potter e a Câmara Secreta", "description": "Segundo livro da saga Harry Potter.", "author": "J. K. Rowling", "genre": "Fantasia", "price": 49.90, "amount": 15},
    {"title": "Harry Potter e o Prisioneiro de Azkaban", "description": "Terceiro livro da saga Harry Potter.", "author": "J. K. Rowling", "genre": "Fantasia", "price": 49.90, "amount": 15},
    {"title": "Harry Potter e o Cálice de Fogo", "description": "Quarto livro da saga Harry Potter.", "author": "J. K. Rowling", "genre": "Fantasia", "price": 59.90, "amount": 15},
    {"title": "Harry Potter e a Ordem da Fênix", "description": "Quinto livro da saga Harry Potter.", "author": "J. K. Rowling", "genre": "Fantasia", "price": 59.90, "amount": 15},
    {"title": "Harry Potter e o Enigma do Príncipe", "description": "Sexto livro da saga Harry Potter.", "author": "J. K. Rowling", "genre": "Fantasia", "price": 59.90, "amount": 15},
    {"title": "Harry Potter e as Relíquias da Morte", "description": "Sétimo livro da saga Harry Potter.", "author": "J. K. Rowling", "genre": "Fantasia", "price": 59.90, "amount": 15},
    {"title": "Dom Casmurro", "description": "Clássico da literatura brasileira.", "author": "Machado de Assis", "genre": "Literatura Clássica", "price": 39.90, "amount": 20},
    {"title": "Memórias Póstumas de Brás Cubas", "description": "Obra-prima de Machado de Assis.", "author": "Machado de Assis", "genre": "Literatura Clássica", "price": 39.90, "amount": 20},
    {"title": "Quincas Borba", "description": "Romance filosófico de Machado de Assis.", "author": "Machado de Assis", "genre": "Romance", "price": 39.90, "amount": 20},
    {"title": "A Hora da Estrela", "description": "Obra marcante de Clarice Lispector.", "author": "Clarice Lispector", "genre": "Romance", "price": 34.90, "amount": 18},
    {"title": "Perto do Coração Selvagem", "description": "Romance de estreia de Clarice Lispector.", "author": "Clarice Lispector", "genre": "Romance", "price": 34.90, "amount": 18},
    {"title": "A Paixão Segundo G.H.", "description": "Um dos romances mais conhecidos de Clarice Lispector.", "author": "Clarice Lispector", "genre": "Romance", "price": 34.90, "amount": 18},
    {"title": "1984", "description": "Distopia clássica sobre totalitarismo.", "author": "George Orwell", "genre": "Ficção Científica", "price": 44.90, "amount": 25},
    {"title": "A Revolução dos Bichos", "description": "Fábula política satírica.", "author": "George Orwell", "genre": "Ficção Científica", "price": 39.90, "amount": 25},
    {"title": "Orgulho e Preconceito", "description": "Clássico romance inglês.", "author": "Jane Austen", "genre": "Romance", "price": 42.90, "amount": 15},
    {"title": "Razão e Sensibilidade", "description": "Outro grande romance de Jane Austen.", "author": "Jane Austen", "genre": "Romance", "price": 42.90, "amount": 15},
    {"title": "Cem Anos de Solidão", "description": "Obra-prima do realismo mágico.", "author": "Gabriel García Márquez", "genre": "Romance", "price": 54.90, "amount": 12},
    {"title": "O Amor nos Tempos do Cólera", "description": "Romance sobre o amor e o tempo.", "author": "Gabriel García Márquez", "genre": "Romance", "price": 54.90, "amount": 12},
    {"title": "Ensaio sobre a Cegueira", "description": "Romance alegórico sobre a sociedade.", "author": "José Saramago", "genre": "Romance", "price": 49.90, "amount": 10},
    {"title": "O Evangelho Segundo Jesus Cristo", "description": "Polêmico romance de Saramago.", "author": "José Saramago", "genre": "Romance", "price": 49.90, "amount": 10},
    {"title": "A Metamorfose", "description": "Clássico da literatura existencialista.", "author": "Franz Kafka", "genre": "Romance", "price": 39.90, "amount": 14},
    {"title": "O Processo", "description": "Romance sobre burocracia e alienação.", "author": "Franz Kafka", "genre": "Romance", "price": 39.90, "amount": 14},
    {"title": "Mrs. Dalloway", "description": "Romance modernista inglês.", "author": "Virginia Woolf", "genre": "Romance", "price": 44.90, "amount": 10},
    {"title": "Ao Farol", "description": "Obra-prima de Virginia Woolf.", "author": "Virginia Woolf", "genre": "Romance", "price": 44.90, "amount": 10},
    {"title": "O Primo Basílio", "description": "Romance realista português.", "author": "José Saramago", "genre": "Romance", "price": 44.90, "amount": 10},
    {"title": "O Mundo de Sofia", "description": "Introdução à filosofia para jovens.", "author": "Jostein Gaarder", "genre": "Infantojuvenil", "price": 39.90, "amount": 20},
    {"title": "O Nome da Rosa", "description": "Romance policial histórico.", "author": "Umberto Eco", "genre": "Mistério", "price": 49.90, "amount": 10},
    {"title": "O Código Da Vinci", "description": "Thriller de mistério e conspiração.", "author": "Dan Brown", "genre": "Mistério", "price": 49.90, "amount": 15},
    {"title": "O Iluminado", "description": "Terror psicológico em um hotel isolado.", "author": "Stephen King", "genre": "Terror", "price": 49.90, "amount": 12},
    {"title": "It: A Coisa", "description": "Terror sobrenatural em uma pequena cidade.", "author": "Stephen King", "genre": "Terror", "price": 59.90, "amount": 12},
    {"title": "Carrie, a Estranha", "description": "Primeiro romance publicado de Stephen King.", "author": "Stephen King", "genre": "Terror", "price": 39.90, "amount": 12},
    {"title": "A Arte da Guerra", "description": "Clássico tratado militar chinês.", "author": "Sun Tzu", "genre": "Negócios", "price": 34.90, "amount": 20},
    {"title": "Odisseia", "description": "Poema épico grego.", "author": "Homero", "genre": "Literatura Clássica", "price": 49.90, "amount": 10},
    {"title": "Ilíada", "description": "Poema épico grego.", "author": "Homero", "genre": "Literatura Clássica", "price": 49.90, "amount": 10},
    {"title": "A República", "description": "Obra filosófica fundamental.", "author": "Platão", "genre": "Filosofia", "price": 44.90, "amount": 10},
    {"title": "Édipo Rei", "description": "Tragédia grega clássica.", "author": "Sófocles", "genre": "Literatura Clássica", "price": 34.90, "amount": 10},
    {"title": "Mensagem", "description": "Obra poética de Fernando Pessoa.", "author": "Fernando Pessoa", "genre": "Poesia", "price": 29.90, "amount": 10},
    {"title": "Alguma Poesia", "description": "Primeiro livro de Carlos Drummond de Andrade.", "author": "Carlos Drummond de Andrade", "genre": "Poesia", "price": 29.90, "amount": 10},
    {"title": "Ficciones", "description": "Coletânea de contos fantásticos.", "author": "Jorge Luis Borges", "genre": "Contos", "price": 39.90, "amount": 10},
    {"title": "O Aleph", "description": "Contos e reflexões filosóficas.", "author": "Jorge Luis Borges", "genre": "Contos", "price": 39.90, "amount": 10},
    {"title": "Sítio do Picapau Amarelo", "description": "Clássico da literatura infantil brasileira.", "author": "Monteiro Lobato", "genre": "Infantojuvenil", "price": 34.90, "amount": 20},
    {"title": "Reinações de Narizinho", "description": "Aventuras no Sítio do Picapau Amarelo.", "author": "Monteiro Lobato", "genre": "Infantojuvenil", "price": 34.90, "amount": 20},
    {"title": "O Caso dos Dez Negrinhos", "description": "Mistério policial de Agatha Christie.", "author": "Agatha Christie", "genre": "Mistério", "price": 39.90, "amount": 15},
    {"title": "Assassinato no Expresso do Oriente", "description": "Clássico romance policial.", "author": "Agatha Christie", "genre": "Mistério", "price": 39.90, "amount": 15},
    {"title": "Grande Sertão: Veredas", "description": "Obra-prima de Guimarães Rosa, um dos maiores romances brasileiros.", "author": "João Guimarães Rosa", "genre": "Literatura Nacional", "price": 49.90, "amount": 15},
    {"title": "Sagarana", "description": "Coletânea de contos de Guimarães Rosa.", "author": "João Guimarães Rosa", "genre": "Contos", "price": 39.90, "amount": 10},
    {"title": "Vidas Secas", "description": "Romance marcante de Graciliano Ramos sobre a seca no sertão.", "author": "Graciliano Ramos", "genre": "Literatura Nacional", "price": 39.90, "amount": 12},
    {"title": "São Bernardo", "description": "Romance psicológico de Graciliano Ramos.", "author": "Graciliano Ramos", "genre": "Romance", "price": 39.90, "amount": 12},
    {"title": "O Alienista", "description": "Sátira de Machado de Assis sobre a loucura e a sociedade.", "author": "Machado de Assis", "genre": "Contos", "price": 29.90, "amount": 18},
    {"title": "A Moreninha", "description": "Primeiro romance do romantismo brasileiro.", "author": "Joaquim Manuel de Macedo", "genre": "Romance", "price": 29.90, "amount": 10},
    {"title": "Senhora", "description": "Romance de José de Alencar sobre amor e dinheiro.", "author": "José de Alencar", "genre": "Romance", "price": 34.90, "amount": 10},
    {"title": "Iracema", "description": "Romance indianista de José de Alencar.", "author": "José de Alencar", "genre": "Romance", "price": 34.90, "amount": 10},
    {"title": "O Guarani", "description": "Romance de aventura e amor no Brasil colonial.", "author": "José de Alencar", "genre": "Aventura", "price": 34.90, "amount": 10},
    {"title": "Capitães da Areia", "description": "Romance de Jorge Amado sobre meninos de rua em Salvador.", "author": "Jorge Amado", "genre": "Literatura Nacional", "price": 39.90, "amount": 12},
    {"title": "Gabriela, Cravo e Canela", "description": "Romance de Jorge Amado ambientado em Ilhéus.", "author": "Jorge Amado", "genre": "Romance", "price": 39.90, "amount": 12},
    {"title": "O Cortiço", "description": "Romance naturalista de Aluísio Azevedo.", "author": "Aluísio Azevedo", "genre": "Literatura Nacional", "price": 34.90, "amount": 10},
    {"title": "A Escrava Isaura", "description": "Romance abolicionista de Bernardo Guimarães.", "author": "Bernardo Guimarães", "genre": "Romance", "price": 29.90, "amount": 10},
    {"title": "O Ateneu", "description": "Romance de Raul Pompeia sobre a vida em um internato.", "author": "Raul Pompeia", "genre": "Romance", "price": 29.90, "amount": 10},
    {"title": "A Divina Comédia", "description": "Poema épico de Dante Alighieri.", "author": "Dante Alighieri", "genre": "Literatura Clássica", "price": 59.90, "amount": 10},
    {"title": "Inferno", "description": "Primeira parte da Divina Comédia.", "author": "Dante Alighieri", "genre": "Literatura Clássica", "price": 39.90, "amount": 10},
    {"title": "Purgatório", "description": "Segunda parte da Divina Comédia.", "author": "Dante Alighieri", "genre": "Literatura Clássica", "price": 39.90, "amount": 10},
    {"title": "Paraíso", "description": "Terceira parte da Divina Comédia.", "author": "Dante Alighieri", "genre": "Literatura Clássica", "price": 39.90, "amount": 10},
    {"title": "O Estrangeiro", "description": "Romance existencialista de Albert Camus.", "author": "Albert Camus", "genre": "Romance", "price": 39.90, "amount": 10},
    {"title": "A Peste", "description": "Romance filosófico de Albert Camus.", "author": "Albert Camus", "genre": "Romance", "price": 39.90, "amount": 10},
    {"title": "O Pequeno Nicolau", "description": "Histórias divertidas de um menino francês.", "author": "René Goscinny", "genre": "Infantojuvenil", "price": 29.90, "amount": 10},
    {"title": "O Apanhador no Campo de Centeio", "description": "Romance de formação de J. D. Salinger.", "author": "J. D. Salinger", "genre": "Romance", "price": 39.90, "amount": 10},
    {"title": "Moby Dick", "description": "Clássico da literatura americana sobre a caça à baleia.", "author": "Herman Melville", "genre": "Aventura", "price": 49.90, "amount": 10},
    {"title": "Drácula", "description": "Romance gótico de Bram Stoker.", "author": "Bram Stoker", "genre": "Terror", "price": 39.90, "amount": 10},
    {"title": "Frankenstein", "description": "Romance gótico de Mary Shelley.", "author": "Mary Shelley", "genre": "Terror", "price": 39.90, "amount": 10},
    {"title": "O Médico e o Monstro", "description": "Clássico do terror psicológico.", "author": "Robert Louis Stevenson", "genre": "Terror", "price": 34.90, "amount": 10},
    {"title": "O Morro dos Ventos Uivantes", "description": "Romance inglês de Emily Brontë.", "author": "Emily Brontë", "genre": "Romance", "price": 39.90, "amount": 10},
    {"title": "Jane Eyre", "description": "Romance inglês de Charlotte Brontë.", "author": "Charlotte Brontë", "genre": "Romance", "price": 39.90, "amount": 10},
    {"title": "O Retrato de Dorian Gray", "description": "Romance de Oscar Wilde sobre vaidade e juventude.", "author": "Oscar Wilde", "genre": "Romance", "price": 39.90, "amount": 10},
    {"title": "Crime e Castigo", "description": "Romance russo de Fiódor Dostoiévski.", "author": "Fiódor Dostoiévski", "genre": "Romance", "price": 49.90, "amount": 10},
    {"title": "Os Irmãos Karamázov", "description": "Último romance de Dostoiévski.", "author": "Fiódor Dostoiévski", "genre": "Romance", "price": 59.90, "amount": 10},
    {"title": "Guerra e Paz", "description": "Romance épico de Liev Tolstói.", "author": "Liev Tolstói", "genre": "Romance", "price": 69.90, "amount": 10},
    {"title": "Anna Kariênina", "description": "Romance russo de Liev Tolstói.", "author": "Liev Tolstói", "genre": "Romance", "price": 59.90, "amount": 10},
    {"title": "O Pequeno Príncipe", "description": "Clássico infantojuvenil.", "author": "Antoine de Saint-Exupéry", "genre": "Infantojuvenil", "price": 29.90, "amount": 30},
]


# Remover duplicações
unique_titles = set()
unique_books = []
for book in books:
    if book["title"] not in unique_titles:
        unique_books.append(book)
        unique_titles.add(book["title"])
books = unique_books


class Command(BaseCommand):
    def handle(self, *args, **options):
        for book in books:
            try:
                writer = Writer.objects.get(fullname=book["author"])
                genre = Genre.objects.get(title=book["genre"])
                obj, created = Book.objects.get_or_create(
                    title=book["title"],
                    defaults={
                        "writer": writer,
                        "genre": genre,
                        "description": book["description"],
                        "price": Decimal(book["price"]),
                        "amount": book["amount"],
                    },
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Livro "{book["title"]}" criado.'))
                else:
                    needs_save = False
                    if obj.writer != writer:
                        obj.writer = writer
                        needs_save = True
                    if obj.genre != genre:
                        obj.genre = genre
                        needs_save = True
                    if obj.description != book["description"]:
                        obj.description = book["description"]
                        needs_save = True
                    if obj.price != Decimal(book["price"]):
                        obj.price = Decimal(book["price"])
                        needs_save = True
                    if obj.amount != book["amount"]:
                        obj.amount = book["amount"]
                        needs_save = True
                    if needs_save:
                        obj.save()
                        self.stdout.write(self.style.WARNING(f'Livro "{book["title"]}" atualizado.'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Livro "{book["title"]}" já existe e está atualizado.'))
            except Writer.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Autor "{book["author"]}" não encontrado.'))
            except Genre.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Gênero "{book["genre"]}" não encontrado.'))
