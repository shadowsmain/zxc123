from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class fantasy(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    release = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фэнтези'
        verbose_name_plural = 'Фэнтези'


class shounen(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    release = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сёнэн'
        verbose_name_plural = 'Сёнэн'

class cyberpank(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    release = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Киберпанк'
        verbose_name_plural = 'Киберпанк'


class thriller(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    release = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Боевик'
        verbose_name_plural = 'Боевик'