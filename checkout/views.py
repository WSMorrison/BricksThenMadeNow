from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import Orderform


def checkout(request):
    cart = request.session.get('cart')
    if not cart:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('items'))

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NNuisE1ZJ5oC3btNsXaNlqOtMmDMMUUGQAXNIlh3WYRIeyL5A41O0fZBlpYyPuicxUAYtkpf3vQlTWgRea5B84I00mitWIOZn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
