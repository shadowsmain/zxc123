# Generated by Django 2.2 on 2020-12-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neoclassica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'неоклассика',
                'verbose_name_plural': 'неоклассика',
            },
        ),
    ]