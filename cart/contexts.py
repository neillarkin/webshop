from django.shortcuts import get_object_or_404
from records.models import Record

"""Displays the Cart context which is available to all webpages/apps"""
def cart_contents(request):
    
    #Request existing cart if it exists or blank cart if not
    cart = request.session.get('cart', {})

    #Initialize cart items
    cart_items = []
    total = 0
    record_count = 0

    #For loop takes record ID and quantity in cart
    for id, quantity in cart.items():
        #get record object using primary key
        record = get_object_or_404(Record, pk=id)
        
        #Calculate total by adding multiplication of quantity with price
        total += quantity * record.price
        
        #increment count as quantity increases
        record_count += quantity
        
        #Append each item  to the cart array/list
        cart_items.append({'id': id, 'quantity': quantity, 'record': record})
    
    #Return a dictionary of key/value pairs
    return {'cart_items': cart_items, 'total': total, 'record_count': record_count}