from django.shortcuts import render

from officeapp.models import Office


def office(request):
    offices = Office.objects.all()
    context = {
        'offices': offices,
        'page_title': 'офисы',
    }

    return render(request, 'officeapp/office.html', context)