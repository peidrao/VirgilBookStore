from django.core.management.base import BaseCommand

from book.models import Writer


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Writer.objects.filter(fullname="J. R. R. Tolkien").exists():
            Writer.objects.create(
                fullname="J. R. R. Tolkien",
                description="John Ronald Reuel Tolkien CBE FRSL was an English writer and philologist. He was the author of the high fantasy works The Hobbit and The Lord of the Rings.",
            )
        if not Writer.objects.filter(fullname="Olavo de Carvalho").exists():
            Writer.objects.create(
                fullname="Olavo de Carvalho",
                description="Olavo Luiz Pimentel de Carvalho GCRB was a Brazilian polemicist, self-proclaimed philosopher, political pundit, former astrologer, journalist, and far-right conspiracy theorist.",
            )
        if not Writer.objects.filter(fullname="Tomás de Aquino").exists():
            Writer.objects.create(
                fullname="Tomás de Aquino",
                description="Thomas Aquinas, OP was an Italian Dominican friar and priest who was an influential philosopher, theologian and jurist in the tradition of scholasticism",
            )
        if not Writer.objects.filter(fullname="René Guénon").exists():
            Writer.objects.create(
                fullname="René Guénon",
                description="René Jean-Marie-Joseph Guénon, also known as Abdalwâhid Yahiâ was a French intellectual who remains an influential figure in the domain of metaphysics",
            )
        if not Writer.objects.filter(fullname="Dante Alighieri").exists():
            Writer.objects.create(
                fullname="Dante Alighieri",
                description="Dante Alighieri, probably baptized Durante di Alighiero degli Alighieri and often referred to as Dante, was an Italian poet, writer and philosopher.",
            )
        if not Writer.objects.filter(fullname="Aristóteles").exists():
            Writer.objects.create(
                fullname="Aristóteles",
                description="Aristotle was a Greek philosopher and polymath during the Classical period in Ancient Greece. Taught by Plato, he was the founder of the Peripatetic school of philosophy within the Lyceum and the wider Aristotelian tradition.",
            )
        if not Writer.objects.filter(fullname="Otto Maria Carpeaux").exists():
            Writer.objects.create(
                fullname="Otto Maria Carpeaux",
                description="Carpeaux was born Otto Karpfen in 1900 in Vienna, Austria-Hungary, to a Jewish family, and lived there until 1939. At the age of 20, he enrolled at the University of Vienna to study Law",
            )
        if not Writer.objects.filter(fullname="Mário Ferreira dos Santos").exists():
            Writer.objects.create(
                fullname="Mário Ferreira dos Santos",
                description="Mário Ferreira dos Santos was a Brazilian philosopher, translator, writer and anarchist activist. Born in Tietê, São Paulo, Ferreira dos Santos was raised in Pelotas, Rio Grande do Sul, and graduated in Law and Social Sciences at the Federal University of Rio Grande do Sul.",
            )
        if not Writer.objects.filter(fullname="Blaise Pascal").exists():
            Writer.objects.create(
                fullname="Blaise Pascal",
                description="He was a child prodigy who was educated by his father, a tax collector in Rouen. Pascals earliest mathematical work was on conic sections; he wrote a significant treatise on the subject of projective geometry at the age of 16.",
            )
        if not Writer.objects.filter(fullname="C. S. Lewis").exists():
            Writer.objects.create(
                fullname="C. S. Lewis",
                description="Clive Staples Lewis was a British writer and Anglican lay theologian. He held academic positions in English literature at both Oxford University and Cambridge University.",
            )
