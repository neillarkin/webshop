from django.test import TestCase
from .models import Genre
"""
Test Genre views are returning expected pages
"""

class TestGenreViews(TestCase):

    def test_get_genre(self):
        page = self.client.get("/genres/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "genres.html")
        
    def test_get_genres_records(self):
        genre = Genre(name="An genre")
        genre.save()
        page = self.client.get("/genres/genres-records/{0}".format(genre.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "genres_records.html")