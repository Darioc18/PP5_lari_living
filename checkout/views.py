from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OyjqBP6K4eNf8rwh7Y8HyXzKgpRUU4qCkcFS3R6p93xRkD2MuEP95JEdFW9KQUvL1HXfoIhhT0CLQZGIzVdcKs300nZ7oCQ4N',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)