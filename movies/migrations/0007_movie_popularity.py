# Generated by Django 3.2 on 2022-05-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20220523_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='popularity',
            field=models.IntegerField(null=True),
        ),
    ]
