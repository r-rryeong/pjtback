# Generated by Django 3.2 on 2022-05-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_comingsoon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boxoffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=20)),
                ('audience', models.CharField(max_length=20)),
                ('poster_path', models.TextField()),
            ],
        ),
    ]