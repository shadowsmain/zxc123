from django.contrib import admin

from mainapp.models import Category, fantasy, shounen, cyberpank, thriller

admin.site.register(Category)
admin.site.register(fantasy)
admin.site.register(shounen)
admin.site.register(cyberpank)
admin.site.register(thriller)