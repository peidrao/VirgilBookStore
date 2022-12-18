from django.core.management.base import BaseCommand

from book.models import Book, Genre, Writer


class Command(BaseCommand):

    def handle(self, *args, **options):
        art = Genre.objects.get(slug="arte")
        comedy = Genre.objects.get(slug="comedia")
        math = Genre.objects.get(slug="matematica")
        fiction = Genre.objects.get(slug="ficcao")
        poetry = Genre.objects.get(slug="poesia")
        policy = Genre.objects.get(slug="politica")
        religion = Genre.objects.get(slug="religiao")
        economy = Genre.objects.get(slug="economia")
        philosophy = Genre.objects.get(slug="filosofia")
        medieval_philosophy = Genre.objects.get(slug="filosofia-medieval")
        stoic_philosophy = Genre.objects.get(slug="filosofia-estoica")
        history = Genre.objects.get(slug="historia")
        brazil_history = Genre.objects.get(slug="historia-do-brasil")
        western_history = Genre.objects.get(slug="historia-do-ocidente")
        africa_history = Genre.objects.get(slug="historia-africana")

        jrrt = Writer.objects.get(fullname='J. R. R. Tolkien')
        oc = Writer.objects.get(fullname='Olavo de Carvalho')
        ta = Writer.objects.get(fullname='Tomás de Aquino')
        rg = Writer.objects.get(fullname='René Guénon')
        da = Writer.objects.get(fullname='Dante Alighieri')
        a = Writer.objects.get(fullname='Aristóteles')
        omc = Writer.objects.get(fullname='Otto Maria Carpeaux')
        mfs = Writer.objects.get(fullname='Mário Ferreira dos Santos')
        csl = Writer.objects.create(fullname='C. S. Lewis')

        if not Book.objects.filter(title='Inferno').exists():
            Book.objects.create(title="Inferno", writer=da, genre=poetry, description="O Inferno é a primeira parte da Divina Comédia de Dante Alighieri, sendo as outras duas o Purgatório e o Paraíso.", price=50, status=1, amount=12)
        if not Book.objects.filter(title='Inferno').exists():
            Book.objects.create(title="Purgatório", writer=da, genre=poetry, description="Purgatório é a segunda parte da Divina Comédia de Dante Alighieri. Está dividido em trinta e três cantos.", price=20, status=1, amount=40)
        if not Book.objects.filter(title='Paraíso').exists():
            Book.objects.create(title="Paraíso", writer=da, genre=poetry, description="Paraíso é a terceira e última parte da Divina Comédia de Dante. É uma alegoria, dizendo da visão de Dante do céu, guiado por Beatriz, amor platônico de Dante.", price=78, status=1, amount=10)
        if not Book.objects.filter(title='Divina Comédia').exists():
            Book.objects.create(title="Divina Comédia", writer=da, genre=poetry, description="Escrito originalmente em italiano vulgar baseado no dialeto toscano da época e bastante semelhante ao italiano atual, e não em latim como fazia-se comum à época, trata-se de um poema articulado por trilogias", price=150, status=1, amount=120)
        
        if not Book.objects.filter(title='O Silmarillion').exists():
            Book.objects.create(title="O Silmarillion", writer=jrrt, genre=fiction, description="O Silmarillion é o relato dos Dias Antigos da Primeira Era do mundo criado por J.R.R. Tolkien", price=44, status=1, amount=33)
        if not Book.objects.filter(title='O Hobbit').exists():
            Book.objects.create(title="O Hobbit", writer=jrrt, genre=fiction, description="Bilbo Bolseiro era um dos mais respeitáveis hobbits de todo o Condado até que, um dia, o mago Gandalf bate à sua porta.", price=31, status=1, amount=2)
        if not Book.objects.filter(title='O Senhor dos Anéis').exists():
            Book.objects.create(title="O Senhor dos Anéis", writer=jrrt, genre=fiction, description="Apesar de ter sido publicado em três volumes – A Sociedade do Anel, As Duas Torres e O Retorno do Rei – desde os anos 1950, O Senhor dos Anéis não é exatamente uma trilogia, mas um único grande romance que só pode ser compreendido em seu conjunto, segundo a concepção de seu autor, J.R.R. Tolkien. ", price=200, status=1, amount=10)
        if not Book.objects.filter(title='A Queda de Gondolin').exists():
            Book.objects.create(title="A Queda de Gondolin", writer=jrrt, genre=fiction, description="O último dos três Grandes Contos Perdidos do legendário de J.R.R.Tolkien narra a jornada de Tuor rumo à cidade secreta de Gondolin, refúgio élfico do povo do Rei Turgon. Contra a bela cidade, levanta-se Morgoth, o Inimigo Sombrio, com seu exército de seres malévolos.", price=35, status=1, amount=19)
        
        if not Book.objects.filter(title='O Jardim das Aflições').exists():
            Book.objects.create(title="O Jardim das Aflições", writer=oc, genre=philosophy, description="A tese fundamental deste monumental ensaio é a de que a história do ocidente é marcada pela ideia de Império e de suas sucessivas tentativas de reestruturação; mesmo com roupagens diferentes, há sempre o mesmo objetivo: ampliar os domínios do Império até os limites do mundo visível.", price=70, status=1, amount=190)
        if not Book.objects.filter(title='A Nova Era e a Revolução Cultural').exists():
            Book.objects.create(title="A Nova Era e a Revolução Cultural", writer=oc, genre=philosophy, description="A Nova Era, da qual Fritjof Capra se tornou festejado porta-voz, e a Revolução Cultural, de Antonio Gramsci, têm algo em comum: ambas pretendem introduzir no espírito humano modificações vastas, profundas e irreversíveis.", price=56, status=1, amount=20)
        if not Book.objects.filter(title='O Imbecil Coletivo: Atualidades Inculturais Brasileiras').exists():
            Book.objects.create(title="O Imbecil Coletivo: Atualidades Inculturais Brasileiras", writer=oc, genre=philosophy, description="Quem é o imbecil coletivo?Ele é duplo: nasce do improvável matrimônio do intelectual pernóstico com a ralé enfurecida.", price=66, status=1, amount=5)
        if not Book.objects.filter(title='A Filosofia e seu Inverso').exists():
            Book.objects.create(title="A Filosofia e seu Inverso", writer=oc, genre=philosophy, description="Mas não só. Olavo de Carvalho nos recorda que não esquecer nossa condição mortal é o ponto de partida da investigação metafísica", price=35, status=1, amount=120)
        if not Book.objects.filter(title='O mínimo que você precisa saber para não ser um idiota').exists():
            Book.objects.create(title="O mínimo que você precisa saber para não ser um idiota", writer=oc, genre=philosophy, description=" O mínimo que você precisa saber para não ser idiota, são uma pequena parcela dos textos assinados pelo filósofo em diversos veículos da imprensa brasileira entre 1997 e 2013.", price=299, status=1, amount=10)
        

        if not Book.objects.filter(title='Verdade e conhecimento').exists():
            Book.objects.create(title="Verdade e conhecimento", writer=ta, genre=philosophy, description="Verdade e conhecimento', em edição bilíngue, apresenta ao leitor o tratamento que Tomás de Aquino dá - nas Quaestiones Disputatae de Veritate ", price=4, status=1, amount=10)
        if not Book.objects.filter(title='Suma Teológica:').exists():
            Book.objects.create(title="Suma Teológica:", writer=ta, genre=philosophy, description="Suma Teológica, a síntese brilhante de Santo Tomás de Aquino do pensamento cristão, teve um impacto decisivo e permanente na filosofia e na religião desde o século XIII.", price=189, status=1, amount=43)
        if not Book.objects.filter(title='A Caridade, a Correção Fraterna e a Esperança').exists():
            Book.objects.create(title="A Caridade, a Correção Fraterna e a Esperança", writer=ta, genre=religion, description="Tomás de Aquino, filósofo e teólogo dominicano, santo e doutor da Igreja, escreveu diversas obras, dentre as mais importantes estão as famosas Questões Disputadas, que são o fruto característico da universidade medieval. ", price=78, status=1, amount=10)
        if not Book.objects.filter(title='O CREDO: EXPLICADO POR SÃO TOMÁS DE AQUINO').exists():
            Book.objects.create(title="O CREDO: EXPLICADO POR SÃO TOMÁS DE AQUINO", writer=ta, genre=religion, description="ão Tomás de Aquino foi um importante teólogo, filósofo e padre dominicano do século XIII. Foi declarado santo pelo papa João XXII em 18 de julho de 1323. ", price=10, status=1, amount=10)
        
        if not Book.objects.filter(title='A Crise do Mundo Moderno').exists():
            Book.objects.create(title="A Crise do Mundo Moderno", writer=rg, genre=religion, description="Essa obra extremamente profética do grande filósofo perenialista René Guénon trata de uma investigação das causas responsáveis pela atual crise no mundo moderno, bem como as suas consequências e possíveis soluções. Mesmo tendo sido publicada pela primeira vez em 1927, a obra continua a ser relevante.", price=18, status=1, amount=10)
        if not Book.objects.filter(title='O Simbolismo da Cruz').exists():
            Book.objects.create(title="O Simbolismo da Cruz", writer=rg, genre=religion, description="Nesta obra, o grande filósofo perenialista René Guénon analisa um dos símbolos mais antigos e mais proeminentes da história da humanidade, a Cruz, sob o ponto de vista metafísico e comparativo da grande tradição primordial, e não do ponto de vista puramente histórico", price=8, status=1, amount=10)
        if not Book.objects.filter(title='O Erro Espírita').exists():
            Book.objects.create(title="O Erro Espírita", writer=rg, genre=religion, description="", price=11, status=1, amount=12)
        
        if not Book.objects.filter(title='Retratos e Leituras').exists():
            Book.objects.create(title="Retratos e Leituras", writer=omc, genre=philosophy, description="Retratos e Leituras é o quarto livro escrito por Otto Maria Carpeaux no Brasil. A primeira edição foi publicada em 1953. ", price=49, status=1, amount=10)
        if not Book.objects.filter(title='História da Literatura Ocidental - Vol. I: A Herança Grego').exists():
            Book.objects.create(title="História da Literatura Ocidental - Vol. I: A Herança Grego", writer=omc, genre=western_history, description="O primeiro volume da História da Literatura Ocidental, de Carpeaux. Neste volume, o autor discorre sobre as literaturas grega e latina.", price=120, status=1, amount=97)
        if not Book.objects.filter(title='Caminhos para Roma: Aventura, queda e vitória do espírito').exists():
            Book.objects.create(title="Caminhos para Roma: Aventura, queda e vitória do espírito", writer=omc, genre=religion, description="Estamos em crise, quer dizer, estamos sem fé. Começou na Reforma, com a autocracia do indivíduo, o caminho funesto que, através do racionalismo, iluminismo, liberalismo, imperialismo, bolchevismo, conduz ainda ao horror do aniquilamento.", price=46, status=1, amount=10)
        
        if not Book.objects.filter(title='Filosofia da Crise').exists():
            Book.objects.create(title="Filosofia da Crise", writer=mfs, genre=policy, description="Ocupando um lugar de destaque na vasta produção do filósofo brasileiro Mário Ferreira dos Santos, Filosofia da Crise é o mais novo lançamento da É Realizações. ", price=33, status=1, amount=40)
        if not Book.objects.filter(title='Invasão Vertical dos Bárbaros ').exists():
            Book.objects.create(title="Invasão Vertical dos Bárbaros ", writer=mfs, genre=philosophy, description="A história nos relata que houve muitas invasões horizontais de bárbaros; hoje, porém, vivemos uma invasão vertical de bárbaros, que é a que penetra pela cultura", price=47, status=1, amount=9)
        if not Book.objects.filter(title='Tratado de Simbólica').exists():
            Book.objects.create(title="Tratado de Simbólica", writer=mfs, genre=philosophy, description="resultado da transcrição de duas palestras de Mário Ferreira dos Santos.", price=12, status=1, amount=20)
            
