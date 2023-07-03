from django.shortcuts import render


def errorpage(request):
    return render(request, 'infopages/errorpage.html')


def shipping(request):
    return render(request, 'infopages/shipping.html')


def faq(request):
    return render(request, 'infopages/faq.html')


def terms(request):
    return render(request, 'infopages/terms.html')
