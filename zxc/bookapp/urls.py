import bookapp.views as bookapp
from django.urls import path

app_name = 'bookapp'

urlpatterns = [
    path('', bookapp.book, name='book'),
]