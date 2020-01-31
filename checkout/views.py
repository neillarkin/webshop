from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from records.models import Record
import stripe


stripe.api_key = settings.STRIPE_SECRET

""" View that validates Checkout form and passes it to Stripe """
@login_required()  # user must be logged in to make a paymnet
def checkout(request):
    if request.method == "POST":
    #user is first shown the order & payment forms
        order_form = OrderForm(request.POST) 
        payment_form = MakePaymentForm(request.POST)
        
    #Validate both forms then save the order form with timestamp
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
        #Get user records purchased from current cart session
            cart = request.session.get('cart', {})
            total = 0 #initialize total to zero
            
        #Loop through cart with ID and quantity
            for id, quantity in cart.items():
                record = get_object_or_404(Record, pk=id) #get Record using PK
                total += quantity * record.price  #calculate quantity and total price
                order_line_item = OrderLineItem(
                    order=order,
                    record=record,
                    quantity=quantity
                )
                order_line_item.save() #save details of items purchased
            
        #Try to make a payment using Stripe API
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100), #Stripe uses cents not euros
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'] #customer id for seller
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('records')) #return to records page
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm() #return blank forms
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, 
    "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
