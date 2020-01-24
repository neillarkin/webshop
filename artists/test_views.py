from django.test import TestCase
from .models import Artist

"""
Test Artist views are returning expected pages
"""

class TestArtistViews(TestCase):

    def test_get_artists(self):
        page = self.client.get("/artists/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artists.html")
    
    def test_get_artists_records(self):
        artist = Artist(name="An artist")
        artist.save()
        page = self.client.get("/artists/artists-records/{0}".format(artist.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artists_records.html")
        
        
    def test_page_where_no_artists_exist(self):
        page = self.client.get("/artists/artists-records/{0}")
        self.assertEqual(page.status_code, 404)
        
