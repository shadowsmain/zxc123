from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'