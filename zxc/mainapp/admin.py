from django.contrib import admin

from mainapp.models import Category, Fantasy, Shounen, Cyberpank, Thriller

admin.site.register(Category)
admin.site.register(Fantasy)
admin.site.register(Shounen)
admin.site.register(Cyberpank)
admin.site.register(Thriller)