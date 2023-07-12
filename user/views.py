from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SiteUser
from .forms import DAAUserform, SiteUserform


# Allows siteuser to view their profile information.
@login_required
def siteuser_profile(request):
    siteuser = get_object_or_404(SiteUser, user=request.user)
    user = siteuser.user

    if request.method == 'POST':
        form = SiteUserform(request.POST, instance=siteuser)
        if form.is_valid():
            form.save()
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


'''
def new_email_signup(request, new_email):

    template = 'account/signup.html'
    context = {
        'new_email': new_email,
    }

    return render(request, template, context)
'''
