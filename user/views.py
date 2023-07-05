from django.shortcuts import render


def siteuser_profile(request):
    template = 'user/siteuser.html'
    context = {}

    return render(request, template, context)
