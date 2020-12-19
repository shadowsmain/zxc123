from django.shortcuts import render

from neoclassicaapp.models import Neoclassica


def neoclassica(request):
    neoclassics = Neoclassica.objects.all()
    context = {
        'neoclassics': neoclassics,
        'page_title': 'неоклассика',
    }

    return render(request, 'neoclassicaapp/neoclassica.html', context)