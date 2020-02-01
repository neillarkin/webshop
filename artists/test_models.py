from django.test import TestCase
from .models import Artist

"""
Test Artist object cn be instantiated

"""

class TestArtistModel(TestCase):

    def test_artist_object_exists(self):
        artist = Artist(name="An artist")
        artist.save()
        self.assertIs(artist.name, "An artist")

    def test_artist_as_string(self):
        artist = Artist(name="An artist")
        self.assertEqual("An artist", str(artist))