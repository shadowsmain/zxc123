from django.db import models


class Neoclassica(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'неоклассика'
        verbose_name_plural = 'неоклассика'