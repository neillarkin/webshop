from django.shortcuts import render, redirect, reverse


"""Renders the cart contents page"""
def view_cart(request):
    """# no Dict returned here because context.py (cart_cotents) is global"""
    return render(request, "cart.html") 

"""Add record qunatity to the cart"""


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity')) #get quantity from records.html form

    cart = request.session.get('cart', {}) #get cart from session (not database)
    if id in cart:
        cart[id] = int(cart[id]) + quantity #if exists, add ID & quantity
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart #update current session cart to this cart instance
    return redirect(reverse('index'))


"""Update the record quantity to the desired amount"""

"""Increase or decrease the quantity in the cart"""
def adjust_cart(request, id):

    quantity = int(request.POST.get('quantity')) #get exisitng quantitiy as an integer
    cart = request.session.get('cart', {}) #get cart from current session

    if quantity > 0:    #if cart is empty then it cannot be adjusted
        cart[id] = quantity
    else:
        cart.pop(id)    #else pop the record id to the end of the list
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
