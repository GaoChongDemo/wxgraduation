# Generated by Django 3.0.5 on 2020-04-19 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0007_movieinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieInfo',
        ),
        migrations.DeleteModel(
            name='TestDemo',
        ),
    ]
