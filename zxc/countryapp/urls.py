import countryapp.views as countryapp
from django.urls import path

app_name = 'countryapp'

urlpatterns = [
    path('', countryapp.country, name='country'),
]