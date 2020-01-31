from django.test import TestCase
from genres.models import Genre

""" Test defaut view for Home Page"""

class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "base.html")
        
    def test_home_page_where_no_records_exist(self):
        page = self.client.get("/99")
        self.assertEqual(page.status_code, 404)