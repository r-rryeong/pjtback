# Generated by Django 3.2 on 2022-05-24 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_boxofficetotal'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BoxofficeTotal',
        ),
    ]
