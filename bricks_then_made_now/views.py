from django.shortcuts import render


def error_404_page(request, exception):

    return render(request, 'error404.html', status=404)


def error_500_page(request):

    return render(request, 'error500.html', status=500)
