"""zxc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import mainapp.views as mainapp
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', mainapp.index, name='index'),
    path('aboutme/', mainapp.aboutme, name='aboutme'),
    path('aboutme/category/<int:pk>/', mainapp.aboutme_page, name='aboutme_page'),
    path('last/', mainapp.last, name='last'),
    path('secretpage/', mainapp.secretpage, name='secret'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', admin.site.urls),
    path ('office/' include('officeapp.urls', namespace='office')),
]
