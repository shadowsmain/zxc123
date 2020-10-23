# Generated by Django 2.2 on 2020-10-23 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201023_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='thriller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True)),
                ('release', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category')),
            ],
            options={
                'verbose_name': 'Боевик',
                'verbose_name_plural': 'Боевик',
            },
        ),
    ]
