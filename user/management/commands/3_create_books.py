from decimal import Decimal
from django.core.management.base import BaseCommand
from book.models import Book, Genre, Writer


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Usando get_or_create para garantir que os objetos existam e evitar duplicação
        genres = {
            "arte": Genre.objects.get_or_create(title="Arte")[0],
            "comedia": Genre.objects.get_or_create(title="Comédia")[0],
            "matematica": Genre.objects.get_or_create(title="Matemática")[0],
            "ficcao": Genre.objects.get_or_create(title="Ficção")[0],
            "poesia": Genre.objects.get_or_create(title="Poesia")[0],
            "politica": Genre.objects.get_or_create(title="Política")[0],
            "religiao": Genre.objects.get_or_create(title="Religião")[0],
            "economia": Genre.objects.get_or_create(title="Economia")[0],
            "filosofia": Genre.objects.get_or_create(title="Filosofia")[0],
            "filosofia-medieval": Genre.objects.get_or_create(
                title="Filosofia Medieval"
            )[0],
            "filosofia-estoica": Genre.objects.get_or_create(
                title="Filosofia Estóica"
            )[0],
            "historia": Genre.objects.get_or_create(title="História")[0],
            "historia-do-brasil": Genre.objects.get_or_create(
                title="História do Brasil"
            )[0],
            "historia-do-ocidente": Genre.objects.get_or_create(
                title="História do Ocidente"
            )[0],
            "historia-africana": Genre.objects.get_or_create(
                title="História Africana"
            )[0],
        }

        writers = {
            "J. R. R. Tolkien": Writer.objects.get_or_create(
                fullname="J. R. R. Tolkien"
            )[0],
            "Olavo de Carvalho": Writer.objects.get_or_create(
                fullname="Olavo de Carvalho"
            )[0],
            "Tomás de Aquino": Writer.objects.get_or_create(fullname="Tomás de Aquino")[
                0
            ],
            "René Guénon": Writer.objects.get_or_create(fullname="René Guénon")[0],
            "Dante Alighieri": Writer.objects.get_or_create(fullname="Dante Alighieri")[
                0
            ],
            "Aristóteles": Writer.objects.get_or_create(fullname="Aristóteles")[0],
            "Otto Maria Carpeaux": Writer.objects.get_or_create(
                fullname="Otto Maria Carpeaux"
            )[0],
            "Mário Ferreira dos Santos": Writer.objects.get_or_create(
                fullname="Mário Ferreira dos Santos"
            )[0],
            "C. S. Lewis": Writer.objects.get_or_create(fullname="C. S. Lewis")[0],
            "Platão": Writer.objects.get_or_create(fullname="Platão")[0],
            "Sêneca": Writer.objects.get_or_create(fullname="Sêneca")[0],
        }

        books_data = [
            {
                "title": "Inferno",
                "writer": writers["Dante Alighieri"],
                "genre": genres["poesia"],
                "description": "O Inferno é a primeira parte da Divina Comédia de Dante Alighieri, sendo as outras duas o Purgatório e o Paraíso.",
                "price": Decimal("50.00"),
                "status": "NEW",
                "amount": 12,
            },
            {
                "title": "Purgatório",
                "writer": writers["Dante Alighieri"],
                "genre": genres["poesia"],
                "description": "Purgatório é a segunda parte da Divina Comédia de Dante Alighieri. Está dividido em trinta e três cantos.",
                "price": Decimal("20.00"),
                "status": "NEW",
                "amount": 40,
            },
            {
                "title": "Paraíso",
                "writer": writers["Dante Alighieri"],
                "genre": genres["poesia"],
                "description": "Paraíso é a terceira e última parte da Divina Comédia de Dante. É uma alegoria, dizendo da visão de Dante do céu, guiado por Beatriz, amor platônico de Dante.",
                "price": Decimal("78.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "Divina Comédia",
                "writer": writers["Dante Alighieri"],
                "genre": genres["poesia"],
                "description": "Escrito originalmente em italiano vulgar baseado no dialeto toscano da época e bastante semelhante ao italiano atual, e não em latim como fazia-se comum à época, trata-se de um poema articulado por trilogias",
                "price": Decimal("150.00"),
                "status": "NEW",
                "amount": 120,
            },
            {
                "title": "O Silmarillion",
                "writer": writers["J. R. R. Tolkien"],
                "genre": genres["ficcao"],
                "description": "O Silmarillion é o relato dos Dias Antigos da Primeira Era do mundo criado por J.R.R. Tolkien",
                "price": Decimal("44.00"),
                "status": "NEW",
                "amount": 33,
            },
            {
                "title": "O Hobbit",
                "writer": writers["J. R. R. Tolkien"],
                "genre": genres["ficcao"],
                "description": "Bilbo Bolseiro era um dos mais respeitáveis hobbits de todo o Condado até que, um dia, o mago Gandalf bate à sua porta.",
                "price": Decimal("31.00"),
                "status": "NEW",
                "amount": 2,
            },
            {
                "title": "O Senhor dos Anéis",
                "writer": writers["J. R. R. Tolkien"],
                "genre": genres["ficcao"],
                "description": "Apesar de ter sido publicado em três volumes – A Sociedade do Anel, As Duas Torres e O Retorno do Rei – desde os anos 1950, O Senhor dos Anéis não é exatamente uma trilogia, mas um único grande romance que só pode ser compreendido em seu conjunto, segundo a concepção de seu autor, J.R.R. Tolkien. ",
                "price": Decimal("200.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "A Queda de Gondolin",
                "writer": writers["J. R. R. Tolkien"],
                "genre": genres["ficcao"],
                "description": "O último dos três Grandes Contos Perdidos do legendário de J.R.R.Tolkien narra a jornada de Tuor rumo à cidade secreta de Gondolin, refúgio élfico do povo do Rei Turgon. Contra a bela cidade, levanta-se Morgoth, o Inimigo Sombrio, com seu exército de seres malévolos.",
                "price": Decimal("35.00"),
                "status": "NEW",
                "amount": 19,
            },
            {
                "title": "O Jardim das Aflições",
                "writer": writers["Olavo de Carvalho"],
                "genre": genres["filosofia"],
                "description": "A tese fundamental deste monumental ensaio é a de que a história do ocidente é marcada pela ideia de Império e de suas sucessivas tentativas de reestruturação; mesmo com roupagens diferentes, há sempre o mesmo objetivo: ampliar os domínios do Império até os limites do mundo visível.",
                "price": Decimal("70.00"),
                "status": "NEW",
                "amount": 190,
            },
            {
                "title": "A Nova Era e a Revolução Cultural",
                "writer": writers["Olavo de Carvalho"],
                "genre": genres["filosofia"],
                "description": "A Nova Era, da qual Fritjof Capra se tornou festejado porta-voz, e a Revolução Cultural, de Antonio Gramsci, têm algo em comum: ambas pretendem introduzir no espírito humano modificações vastas, profundas e irreversíveis.",
                "price": Decimal("56.00"),
                "status": "NEW",
                "amount": 20,
            },
            {
                "title": "O Imbecil Coletivo: Atualidades Inculturais Brasileiras",
                "writer": writers["Olavo de Carvalho"],
                "genre": genres["filosofia"],
                "description": "Quem é o imbecil coletivo?Ele é duplo: nasce do improvável matrimônio do intelectual pernóstico com a ralé enfurecida.",
                "price": Decimal("66.00"),
                "status": "NEW",
                "amount": 5,
            },
            {
                "title": "A Filosofia e seu Inverso",
                "writer": writers["Olavo de Carvalho"],
                "genre": genres["filosofia"],
                "description": "Mas não só. Olavo de Carvalho nos recorda que não esquecer nossa condição mortal é o ponto de partida da investigação metafísica",
                "price": Decimal("35.00"),
                "status": "NEW",
                "amount": 120,
            },
            {
                "title": "O mínimo que você precisa saber para não ser um idiota",
                "writer": writers["Olavo de Carvalho"],
                "genre": genres["filosofia"],
                "description": " O mínimo que você precisa saber para não ser idiota, são uma pequena parcela dos textos assinados pelo filósofo em diversos veículos da imprensa brasileira entre 1997 e 2013.",
                "price": Decimal("299.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "Verdade e conhecimento",
                "writer": writers["Tomás de Aquino"],
                "genre": genres["filosofia"],
                "description": "Verdade e conhecimento', em edição bilíngue, apresenta ao leitor o tratamento que Tomás de Aquino dá - nas Quaestiones Disputatae de Veritate ",
                "price": Decimal("4.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "Suma Teológica:",
                "writer": writers["Tomás de Aquino"],
                "genre": genres["filosofia"],
                "description": "Suma Teológica, a síntese brilhante de Santo Tomás de Aquino do pensamento cristão, teve um impacto decisivo e permanente na filosofia e na religião desde o século XIII.",
                "price": Decimal("189.00"),
                "status": "NEW",
                "amount": 43,
            },
            {
                "title": "A Caridade, a Correção Fraterna e a Esperança",
                "writer": writers["Tomás de Aquino"],
                "genre": genres["religiao"],
                "description": "Tomás de Aquino, filósofo e teólogo dominicano, santo e doutor da Igreja, escreveu diversas obras, dentre as mais importantes estão as famosas Questões Disputadas, que são o fruto característico da universidade medieval. ",
                "price": Decimal("78.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "O CREDO: EXPLICADO POR SÃO TOMÁS DE AQUINO",
                "writer": writers["Tomás de Aquino"],
                "genre": genres["religiao"],
                "description": "ão Tomás de Aquino foi um importante teólogo, filósofo e padre dominicano do século XIII. Foi declarado santo pelo papa João XXII em 18 de julho de 1323. ",
                "price": Decimal("10.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "A Crise do Mundo Moderno",
                "writer": writers["René Guénon"],
                "genre": genres["religiao"],
                "description": "Essa obra extremamente profética do grande filósofo perenialista René Guénon trata de uma investigação das causas responsáveis pela atual crise no mundo moderno, bem como as suas consequências e possíveis soluções. Mesmo tendo sido publicada pela primeira vez em 1927, a obra continua a ser relevante.",
                "price": Decimal("18.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "O Simbolismo da Cruz",
                "writer": writers["René Guénon"],
                "genre": genres["religiao"],
                "description": "Nesta obra, o grande filósofo perenialista René Guénon analisa um dos símbolos mais antigos e mais proeminentes da história da humanidade, a Cruz, sob o ponto de vista metafísico e comparativo da grande tradição primordial, e não do ponto de vista puramente histórico",
                "price": Decimal("8.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "O Erro Espírita",
                "writer": writers["René Guénon"],
                "genre": genres["religiao"],
                "description": "",
                "price": Decimal("11.00"),
                "status": "NEW",
                "amount": 12,
            },
            {
                "title": "Retratos e Leituras",
                "writer": writers["Otto Maria Carpeaux"],
                "genre": genres["filosofia"],
                "description": "Retratos e Leituras é o quarto livro escrito por Otto Maria Carpeaux no Brasil. A primeira edição foi publicada em 1953. ",
                "price": Decimal("49.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "História da Literatura Ocidental - Vol. I: A Herança Grego",
                "writer": writers["Otto Maria Carpeaux"],
                "genre": genres["historia-do-ocidente"],
                "description": "O primeiro volume da História da Literatura Ocidental, de Carpeaux. Neste volume, o autor discorre sobre as literaturas grega e latina.",
                "price": Decimal("120.00"),
                "status": "NEW",
                "amount": 97,
            },
            {
                "title": "Caminhos para Roma: Aventura, queda e vitória do espírito",
                "writer": writers["Otto Maria Carpeaux"],
                "genre": genres["religiao"],
                "description": "Estamos em crise, quer dizer, estamos sem fé. Começou na Reforma, com a autocracia do indivíduo, o caminho funesto que, através do racionalismo, iluminismo, liberalismo, imperialismo, bolchevismo, conduz ainda ao horror do aniquilamento.",
                "price": Decimal("46.00"),
                "status": "NEW",
                "amount": 10,
            },
            {
                "title": "Filosofia da Crise",
                "writer": writers["Mário Ferreira dos Santos"],
                "genre": genres["politica"],
                "description": "Ocupando um lugar de destaque na vasta produção do filósofo brasileiro Mário Ferreira dos Santos, Filosofia da Crise é o mais novo lançamento da É Realizações. ",
                "price": Decimal("33.00"),
                "status": "NEW",
                "amount": 40,
            },
            {
                "title": "Invasão Vertical dos Bárbaros ",
                "writer": writers["Mário Ferreira dos Santos"],
                "genre": genres["filosofia"],
                "description": "A história nos relata que houve muitas invasões horizontais de bárbaros; hoje, porém, vivemos uma invasão vertical de bárbaros, que é a que penetra pela cultura",
                "price": Decimal("47.00"),
                "status": "NEW",
                "amount": 9,
            },
            {
                "title": "Tratado de Simbólica",
                "writer": writers["Mário Ferreira dos Santos"],
                "genre": genres["filosofia"],
                "description": "resultado da transcrição de duas palestras de Mário Ferreira dos Santos.",
                "price": Decimal("12.00"),
                "status": "NEW",
                "amount": 20,
            },
            # Livros de C.S. Lewis
            {
                "title": "As Crônicas de Nárnia",
                "writer": writers["C. S. Lewis"],
                "genre": genres["ficcao"],
                "description": "Viagens ao fim do mundo, criaturas fantásticas e batalhas épicas entre o bem e o mal - o que mais um leitor poderia querer de um livro? O livro que tem tudo isso é O Leão, a Feiticeira e o Guarda-Roupa, escrito em 1950 por C. S. Lewis.",
                "price": Decimal("80.00"),
                "status": "NEW",
                "amount": 25,
            },
            {
                "title": "Cristianismo Puro e Simples",
                "writer": writers["C. S. Lewis"],
                "genre": genres["religiao"],
                "description": "Um dos maiores clássicos do pensamento cristão, esta obra foi adaptada de uma série de programas de rádio produzidos pela BBC durante a Segunda Guerra Mundial.",
                "price": Decimal("45.00"),
                "status": "NEW",
                "amount": 30,
            },
            {
                "title": "Cartas de um diabo a seu aprendiz",
                "writer": writers["C. S. Lewis"],
                "genre": genres["religiao"],
                "description": "Irônica, astuta e original, esta obra-prima da sátira é a correspondência entre um diabo e seu sobrinho, um demônio júnior.",
                "price": Decimal("38.00"),
                "status": "NEW",
                "amount": 15,
            },
            # Livros de Filosofia Clássica
            {
                "title": "A República",
                "writer": writers["Platão"],
                "genre": genres["filosofia"],
                "description": "A República é um diálogo socrático escrito por Platão, filósofo grego, por volta de 380 a.C. É uma das obras mais influentes da filosofia e da teoria política.",
                "price": Decimal("65.00"),
                "status": "NEW",
                "amount": 20,
            },
            {
                "title": "Sobre a Brevidade da Vida",
                "writer": writers["Sêneca"],
                "genre": genres["filosofia-estoica"],
                "description": "Um dos textos mais importantes da filosofia estoica, onde Sêneca argumenta que a vida não é curta, mas nós a tornamos assim.",
                "price": Decimal("25.00"),
                "status": "NEW",
                "amount": 50,
            },
            {
                "title": "Ética a Nicômaco",
                "writer": writers["Aristóteles"],
                "genre": genres["filosofia"],
                "description": "Principal obra de Aristóteles sobre ética. Nela, o filósofo expõe sua concepção de eudaimonia (felicidade) como a finalidade da vida humana.",
                "price": Decimal("55.00"),
                "status": "NEW",
                "amount": 18,
            },
        ]

        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                title=book_data["title"],
                defaults={
                    "writer": book_data["writer"],
                    "genre": book_data["genre"],
                    "description": book_data["description"],
                    "price": book_data["price"],
                    "status": book_data["status"],
                    "amount": book_data["amount"],
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Livro "{book.title}" criado com sucesso.')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Livro "{book.title}" já existe.')
                )

        self.stdout.write(self.style.SUCCESS("Comando finalizado."))
