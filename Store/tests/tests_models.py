from django.test import TestCase

from book.models import Genre


class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(
            title="Terror",
            slug="terror"
        )

    def test_retorno_str(self):
        p1 = Genre.objects.get(title="Terror")
        self.assertEquals(p1.__str__(), 'Terror')
