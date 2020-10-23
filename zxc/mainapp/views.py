from django.shortcuts import render


from mainapp.models import Category



def index(request):
    return render(request, 'mainapp/index.html')


def aboutme(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'mainapp/aboutme.html', context)


def last(request):
    return render(request, 'mainapp/last.html')


def secretpage(request):
    return render(request, 'mainapp/secretpage.html')