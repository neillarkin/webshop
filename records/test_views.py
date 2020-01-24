from django.test import TestCase
from .models import Record

"""
Test view page returns with Record objects
"""

class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "records.html")
        
    def test_home_page_where_no_records_exist(self):
        page = self.client.get("/0")
        self.assertEqual(page.status_code, 404)
        
        
      