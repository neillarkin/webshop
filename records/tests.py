from django.test import TestCase
from .models import Record

# Create your tests here.
class RecordTests(TestCase):

    def test_str(self):
        test_name = Record(name='A record')
        self.assertEqual(str(test_name), 'A record')