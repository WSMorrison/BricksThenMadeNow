import json
import time
import stripe
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from product.models import Sku, Item
from user.models import SiteUser
from .models import Order, LineItem


# Handles Stripe webhook integration and takes action when listener hears an event.
class StripeWH_Handler:

    print('Hello. Is it me you\'re looking for?')
    print('webhook handler start')

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        print('email should get sent')
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

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        print('handling payment succeeded')
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
           intent.latest_charge
        )

        print('payment succeeded wh handler stuff:')
        billing_details = stripe_charge.billing_details
        print('billing_details', billing_details)
        shipping_details = intent.shipping
        print('shipping details', shipping_details)
        grand_total = round(stripe_charge.amount / 100, 2)
        print('grand total', grand_total)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            print('if username is not anon')
            profile = SiteUser.objects.get(user__username=username)
            print('profile')
            if save_info:
                print('if save info whhandler')
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()
                print('profile saved wh handler')
                print('profile.postcode')

        order_exists = False
        attempt = 1
        while attempt <= 5:
            print('wh while')
            try:
                print('wh try')
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    zipcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    state__iexact=shipping_details.address.state,
                    #grand_total=grand_total,
                    #original_cart=cart,
                    #stripe_pid=pid,
                )
                order_exists = True
                print('order_exists')
                break
            except Order.DoesNotExist:
                print('except')
                attempt += 1
                time.sleep(1)
        if order_exists:
            print('if order exists')
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            print('else order doesnt exist')
            order = None
            try:
                print('print else order doesnt exist try')
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
                print('order', order)
                for item_id, item_data in json.loads(cart).items():
                    print('for itemid in json cart, wh handler')
                    sku = Sku.objects.get(id=item_id)
                    item = sku.sku_item                    
                    order_line_item = LineItem(
                        order=order,
                        item=item,
                        sku=sku,
                        quantity=item_data,
                    )
                    order_line_item.save()
                    print('order_line item', order_line_item)
            except Exception as e:
                print(e)
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Payment Succeeded webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Payment Failed webhook received: {event["type"]}',
            status=200)
