import neoclassicaapp.views as neoclassicaapp
from django.urls import path

app_name = 'neoclassicaapp'

urlpatterns = [
    path('', neoclassicaapp.neoclassica, name='neoclassica'),
]