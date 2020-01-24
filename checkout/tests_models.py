from django.test import TestCase
from .models import Order

"""
Test Order object as string and its string attribute

"""

class TestOrderModel(TestCase):

    def test_order_model(self):
        order = Order(id=1, full_name="fred smith", phone_number="123456789", country="ireland", 
        postcode="qaz123", town_or_city="dublin", street_address1="dublin", street_address2="dublin", county="ireland", date="12-12-12")
        self.assertEqual(order.full_name, "fred smith")
        self.assertEqual(order.phone_number, "123456789")
        self.assertEqual(order.country, "ireland")
        self.assertEqual(order.postcode, "qaz123")
        self.assertEqual(order.town_or_city, "dublin")
        self.assertEqual(order.street_address1, "dublin")
        self.assertEqual(order.street_address2, "dublin")
        self.assertEqual(order.county, "ireland")
        self.assertEqual(order.date, "12-12-12")