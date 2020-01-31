from django.db import models
from records.models import Record

""" Represents customer information for each order instance"""
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    # Return a string summary of the order with ID, date and user name"
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


    # Represents the ordered item, the user and the quantity 
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False) #FK to Order class (above)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=False) #FK to Record instance)
    quantity = models.IntegerField(blank=False) 

    # Return instance details as a string
    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.record.name, self.record.price)