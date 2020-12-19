from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128)
    capital = models.CharField(max_length=128)
    language = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'