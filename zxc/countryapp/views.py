from django.shortcuts import render

from countryapp.models import Country


def country(request):
    countrys = Country.objects.all()
    context = {
        'countrys': countrys,
        'page_title': 'страны',
    }

    return render(request, 'countryapp/country.html', context)