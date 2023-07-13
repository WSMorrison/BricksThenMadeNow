from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SiteUser
from .forms import DAAUserform, SiteUserform, NewsletterUserform


# Allows siteuser to view their profile information.
@login_required
def siteuser_profile(request):
    siteuser = get_object_or_404(SiteUser, user=request.user)
    user = siteuser.user

    if request.method == 'POST':
        site_form = SiteUserform(request.POST, instance=siteuser)
        daa_form = DAAUserform(request.POST, instance=user)
        if site_form.is_valid():
            if daa_form.is_valid():
                site_form.save()
                daa_form.save()
                messages.success(request, 'Your information was updated.')

    siteuser_form = SiteUserform(instance=siteuser)
    daauser_form = DAAUserform(instance=user)

    template = 'user/siteuser.html'
    context = {
        'siteuser': siteuser,
        'siteuser_form': siteuser_form,
        'daauser_form': daauser_form,
    }

    return render(request, template, context)


# Allows siteuser to view their order history.
@login_required
def siteuser_order_history(request):
    siteuser = get_object_or_404(SiteUser, user=request.user)
    order_history = siteuser.orders.all().order_by('-date')

    template = 'user/order-history.html'
    context = {
        'siteuser': siteuser,
        'order_history': order_history,
    }

    return render(request, template, context)


def newsletter_signup(request):

    def _send_confirmation_email(email):
        print(email)
        cust_email = email
        subject = render_to_string(
            'user/newsletter_emails/newsletter_confirmation_subject.txt',
        )
        body = render_to_string(
            'user/newsletter_emails/newsletter_confirmation_body.txt',
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
            )

    form = NewsletterUserform

    if request.method == 'POST':
        form = NewsletterUserform(request.POST)
        if form.is_valid():
            email = form.instance.newsletter_email
            form.save()
            messages.success(request, 'Our mailing list was updated.')
            _send_confirmation_email(email)

            return redirect(reverse('home'))

    template = 'user/newsletter-signup.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
