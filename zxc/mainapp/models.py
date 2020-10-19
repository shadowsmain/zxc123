from django.db import models

# Create your models here.

from django.db import models

class SubjectCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)