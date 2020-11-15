from django.shortcuts import render


from mainapp.models import Category, Fantasy, Course



def index(request):
    return render(request, 'mainapp/index.html')


def aboutme(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'mainapp/aboutme.html', context)


def last(request, pk):
    course = Category.objects.fliter(category_id=pk)
    context = {
       'course': course,
        'page_title':'страница каталога'
    }
    return render(request, 'mainapp/last.html', context)


def secretpage(request):
    return render(request, 'mainapp/secretpage.html')

def aboutme_page(request, pk):
    course = Category.objects.filter(category_id=pk)
    context = {
        'Fantasy': Fantasy,
        'page_title': 'страница каталога'
    }
    return render(request, 'mainapp/aboutme_page.html', context)