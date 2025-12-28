from django.core.management.base import BaseCommand
from book.models import Writer

authors = [
    {
        "fullname": "J. R. R. Tolkien",
        "description": "John Ronald Reuel Tolkien CBE FRSL was an English writer and philologist. He was the author of the high fantasy works The Hobbit and The Lord of the Rings.",
    },
    {
        "fullname": "Olavo de Carvalho",
        "description": "Olavo Luiz Pimentel de Carvalho GCRB was a Brazilian polemicist, self-proclaimed philosopher, political pundit, former astrologer, journalist, and far-right conspiracy theorist.",
    },
    {
        "fullname": "Tomás de Aquino",
        "description": "Thomas Aquinas, OP was an Italian Dominican friar and priest who was an influential philosopher, theologian and jurist in the tradition of scholasticism.",
    },
    {
        "fullname": "René Guénon",
        "description": "René Jean-Marie-Joseph Guénon, also known as Abdalwâhid Yahiâ was a French intellectual who remains an influential figure in the domain of metaphysics.",
    },
    {
        "fullname": "Dante Alighieri",
        "description": "Dante Alighieri, probably baptized Durante di Alighiero degli Alighieri and often referred to as Dante, was an Italian poet, writer and philosopher.",
    },
    {
        "fullname": "Aristóteles",
        "description": "Aristotle was a Greek philosopher and polymath during the Classical period in Ancient Greece. Taught by Plato, he was the founder of the Peripatetic school of philosophy within the Lyceum and the wider Aristotelian tradition.",
    },
    {
        "fullname": "Otto Maria Carpeaux",
        "description": "Carpeaux was born Otto Karpfen in 1900 in Vienna, Austria-Hungary, to a Jewish family, and lived there until 1939. At the age of 20, he enrolled at the University of Vienna to study Law.",
    },
    {
        "fullname": "Mário Ferreira dos Santos",
        "description": "Mário Ferreira dos Santos was a Brazilian philosopher, translator, writer and anarchist activist. Born in Tietê, São Paulo, Ferreira dos Santos was raised in Pelotas, Rio Grande do Sul, and graduated in Law and Social Sciences at the Federal University of Rio Grande do Sul.",
    },
    {
        "fullname": "Blaise Pascal",
        "description": "He was a child prodigy who was educated by his father, a tax collector in Rouen. Pascal's earliest mathematical work was on conic sections; he wrote a significant treatise on the subject of projective geometry at the age of 16.",
    },
    {
        "fullname": "C. S. Lewis",
        "description": "Clive Staples Lewis was a British writer and Anglican lay theologian. He held academic positions in English literature at both Oxford University and Cambridge University.",
    },
    {"fullname": "Machado de Assis", "description": "Joaquim Maria Machado de Assis was a Brazilian novelist, poet, playwright, and short story writer, widely regarded as the greatest writer of Brazilian literature."},
    {"fullname": "Clarice Lispector", "description": "Clarice Lispector was a Brazilian novelist and short story writer acclaimed internationally for her innovative novels and short stories."},
    {"fullname": "George Orwell", "description": "Eric Arthur Blair, known by his pen name George Orwell, was an English novelist, essayist, journalist and critic, best known for Animal Farm and 1984."},
    {"fullname": "Jane Austen", "description": "Jane Austen was an English novelist known primarily for her six major novels, including Pride and Prejudice and Sense and Sensibility."},
    {"fullname": "J. K. Rowling", "description": "Joanne Rowling, known by her pen name J. K. Rowling, is a British author, best known for writing the Harry Potter fantasy series."},
    {"fullname": "Gabriel García Márquez", "description": "Gabriel García Márquez was a Colombian novelist, short-story writer, screenwriter and journalist, known affectionately as Gabo throughout Latin America."},
    {"fullname": "Franz Kafka", "description": "Franz Kafka was a German-speaking Bohemian writer, widely regarded as one of the major figures of 20th-century literature."},
    {"fullname": "José Saramago", "description": "José Saramago was a Portuguese writer and recipient of the 1998 Nobel Prize in Literature."},
    {"fullname": "Virginia Woolf", "description": "Adeline Virginia Woolf was an English writer, considered one of the most important modernist 20th-century authors."},
    {"fullname": "Lima Barreto", "description": "Afonso Henriques de Lima Barreto was a Brazilian novelist and journalist, known for his critical works on Brazilian society."},
    {"fullname": "Graciliano Ramos", "description": "Graciliano Ramos de Oliveira was a Brazilian modernist writer, politician and journalist."},
    {"fullname": "Monteiro Lobato", "description": "José Bento Renato Monteiro Lobato was a Brazilian writer, known for his children's books set in the fictional Sítio do Picapau Amarelo."},
    {"fullname": "Agatha Christie", "description": "Dame Agatha Mary Clarissa Christie was an English writer known for her sixty-six detective novels and fourteen short story collections."},
    {"fullname": "Stephen King", "description": "Stephen Edwin King is an American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels."},
    {"fullname": "Sun Tzu", "description": "Sun Tzu was a Chinese general, military strategist, writer, and philosopher who is traditionally credited as the author of The Art of War."},
    {"fullname": "Homero", "description": "Homer was the author of the Iliad and the Odyssey, two epic poems that are the central works of ancient Greek literature."},
    {"fullname": "Platão", "description": "Plato was an ancient Greek philosopher, student of Socrates and teacher of Aristotle, founder of the Academy in Athens."},
    {"fullname": "Sófocles", "description": "Sophocles was an ancient Greek tragedian, one of three ancient Greek tragedians whose plays have survived."},
    {"fullname": "Fernando Pessoa", "description": "Fernando Pessoa was a Portuguese poet, writer, literary critic, translator, publisher and philosopher."},
    {"fullname": "Carlos Drummond de Andrade", "description": "Carlos Drummond de Andrade was a Brazilian poet and writer, considered one of the most influential Brazilian poets of the 20th century."},
    {"fullname": "Jorge Luis Borges", "description": "Jorge Francisco Isidoro Luis Borges was an Argentine short-story writer, essayist, poet and translator, and a key figure in Spanish-language literature."},
]

authors += [
    {"fullname": "Jostein Gaarder", "description": "Jostein Gaarder é um escritor norueguês, autor de livros de ficção e literatura infantojuvenil, conhecido mundialmente por 'O Mundo de Sofia'."},
    {"fullname": "Umberto Eco", "description": "Umberto Eco foi um escritor, filósofo, semiólogo e professor universitário italiano, autor de 'O Nome da Rosa'."},
    {"fullname": "Dan Brown", "description": "Dan Brown é um escritor norte-americano de suspense, famoso por 'O Código Da Vinci'."},
    {"fullname": "João Guimarães Rosa", "description": "João Guimarães Rosa foi um dos maiores escritores brasileiros, autor de 'Grande Sertão: Veredas'."},
    {"fullname": "Joaquim Manuel de Macedo", "description": "Joaquim Manuel de Macedo foi um escritor, médico e professor brasileiro, autor de 'A Moreninha'."},
    {"fullname": "José de Alencar", "description": "José de Alencar foi um dos mais importantes romancistas brasileiros, autor de 'Iracema', 'Senhora' e 'O Guarani'."},
    {"fullname": "Jorge Amado", "description": "Jorge Amado foi um dos mais famosos escritores brasileiros, autor de 'Gabriela, Cravo e Canela' e 'Capitães da Areia'."},
    {"fullname": "Aluísio Azevedo", "description": "Aluísio Azevedo foi um escritor, caricaturista e diplomata brasileiro, autor de 'O Cortiço'."},
    {"fullname": "Bernardo Guimarães", "description": "Bernardo Guimarães foi um escritor e poeta brasileiro, autor de 'A Escrava Isaura'."},
    {"fullname": "Raul Pompeia", "description": "Raul Pompeia foi um escritor brasileiro, autor de 'O Ateneu'."},
    {"fullname": "Albert Camus", "description": "Albert Camus foi um escritor, filósofo e jornalista francês, autor de 'O Estrangeiro' e 'A Peste'."},
    {"fullname": "René Goscinny", "description": "René Goscinny foi um escritor e editor francês, famoso por criar 'O Pequeno Nicolau' e 'Asterix'."},
    {"fullname": "J. D. Salinger", "description": "Jerome David Salinger foi um escritor norte-americano, autor de 'O Apanhador no Campo de Centeio'."},
    {"fullname": "Herman Melville", "description": "Herman Melville foi um escritor norte-americano, autor de 'Moby Dick'."},
    {"fullname": "Bram Stoker", "description": "Bram Stoker foi um escritor irlandês, autor de 'Drácula'."},
    {"fullname": "Mary Shelley", "description": "Mary Shelley foi uma escritora britânica, autora de 'Frankenstein'."},
    {"fullname": "Robert Louis Stevenson", "description": "Robert Louis Stevenson foi um escritor escocês, autor de 'O Médico e o Monstro'."},
    {"fullname": "Emily Brontë", "description": "Emily Brontë foi uma escritora inglesa, autora de 'O Morro dos Ventos Uivantes'."},
    {"fullname": "Charlotte Brontë", "description": "Charlotte Brontë foi uma escritora inglesa, autora de 'Jane Eyre'."},
    {"fullname": "Oscar Wilde", "description": "Oscar Wilde foi um escritor, poeta e dramaturgo irlandês, autor de 'O Retrato de Dorian Gray'."},
    {"fullname": "Fiódor Dostoiévski", "description": "Fiódor Dostoiévski foi um escritor russo, autor de 'Crime e Castigo' e 'Os Irmãos Karamázov'."},
    {"fullname": "Liev Tolstói", "description": "Liev Tolstói foi um escritor russo, autor de 'Guerra e Paz' e 'Anna Kariênina'."},
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for author in authors:
            obj, created = Writer.objects.get_or_create(
                fullname=author["fullname"],
                defaults={"description": author["description"]},
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Autor "{author["fullname"]}" criado.'))
            else:
                # Atualiza descrição se necessário
                if obj.description != author["description"]:
                    obj.description = author["description"]
                    obj.save()
                    self.stdout.write(self.style.WARNING(f'Autor "{author["fullname"]}" atualizado.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Autor "{author["fullname"]}" já existe e está atualizado.'))
