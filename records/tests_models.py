from django.test import TestCase
from .models import Record, Artist, Genre

"""
Test Record objects as string and it other attributes


"""

class test_record_model(TestCase):
    
    def test_record_model_as_string(self):
        record = Record(name="A Record")
        self.assertEqual("A Record", str(record))

    def test_record_model(self):
        artist= Artist(name="An Artist")
        record = Record(id=1, name="A record", description="A description", price="20", 
        image=False, artist=artist)
        self.assertEqual(record.name, "A record")
        self.assertEqual(record.description, "A description")
        self.assertEqual(record.price, "20")
        self.assertFalse(record.image, False)
        self.assertIs(record.artist, artist)
        