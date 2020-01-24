from django.test import TestCase
from .models import Genre

"""
Test Genre object as string and its string attribute

"""

class TestGenreModel(TestCase):

    def test_genre_object_exists(self):
        genre = Genre(name="An genre")
        genre.save()
        self.assertIs(genre.name, "An genre")

    def test_genre_as_string(self):
        genre = Genre(name="An genre")
        self.assertEqual("An genre", str(genre))