from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, LineItem
from product.models import Sku, Item
import stripe
import json
import time


class StripeWH_Handler:

    print('WHHandler start')
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/email_confirmation_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/email_confirmation_body.txt',
            {'order': order}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
        )
        print('Im just an emailin fool')

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        print('WHhandler handle payment intent succeeded')
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
           intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                # The problem is HERE
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    # zipcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    state__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                print('Order exists is true line 78')
                order_exists = True
                break
            except Order.DoesNotExist:
                print('That aint exist')
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            print('There should have just been an email by handler.')
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            print('WHHandler doing it by itself.')
            order = None
            try:
                print('trying some stuff')
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    zipcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    state=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    sku = Sku.objects.get(id=item_id)
                    item = sku.sku_item
                    print(sku, order, item_data, item_id)
                    order_line_item = LineItem(
                        order=order,
                        item=item,
                        sku=sku,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                print('some stuff failed')
                print(e)
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(order)
        print('There should have just been an email by webhook.')
        return HttpResponse(
            content=f'Payment Succeeded webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Payment Failed webhook received: {event["type"]}',
            status=200)
