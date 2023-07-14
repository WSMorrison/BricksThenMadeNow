from django.shortcuts import render


# Directs browser to the generic errorpage.
def errorpage(request):
    return render(request, 'infopages/errorpage.html')


# Directs browser to the shipping information page.
def privacy(request):
    return render(request, 'infopages/privacy.html')


# Directs browser to the Bricks Then Made Now information page.
def faq(request):
    return render(request, 'infopages/faq.html')


# Directs browser to the Terms of Service page.
def terms(request):
    return render(request, 'infopages/terms.html')
