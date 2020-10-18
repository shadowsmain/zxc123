from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def aboutme(request):
    return render(request, 'mainapp/aboutme.html')


def last(request):
    return render(request, 'mainapp/last.html')

def secretpage(request):
    return render(request, 'mainapp/secretpage.html')