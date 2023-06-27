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
    }

    return render(request, template, context)
