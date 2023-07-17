from django.shortcuts import render


# Index/home page
def index(request):

    return render(request, 'home/index.html')
