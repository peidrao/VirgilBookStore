from django.test import TestCase

from book.models import Genre



class BookTestCase(TestCase):
    def setUp(self):
        pass



class GenreTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(title='Comedy')

    def test_create_genre(self):
        self.assertEqual(self.genre.title, 'Comedy')