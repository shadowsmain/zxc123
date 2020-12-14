import officeapp.views as officeapp
from django.urls import path

app_name = 'officeapp'

urlpatterns = [
    path('', officetapp.student, name='office'),
]