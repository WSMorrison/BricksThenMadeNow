from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import SiteUser
from .forms import SiteUserform


# Allows siteuser to view their profile information.
def siteuser_profile(request):
    siteuser = get_object_or_404(SiteUser, user=request.user)

    if request.method == 'POST':
        form = SiteUserform(request.POST, instance=siteuser)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your information was updated.')

    form = SiteUserform(instance=siteuser)

    template = 'user/siteuser.html'
    context = {
        'siteuser': siteuser,
        'form': form,
    }

    return render(request, template, context)


# Allows siteuser to view their order history.
def siteuser_order_history(request):
    siteuser = get_object_or_404(SiteUser, user=request.user)
    order_history = siteuser.orders.all()

    template = 'user/order-history.html'
    context = {
        'siteuser': siteuser,
        'order_history': order_history,
    }

    return render(request, template, context)
