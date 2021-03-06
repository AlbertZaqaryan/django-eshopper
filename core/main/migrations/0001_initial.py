# Generated by Django 4.0.6 on 2022-07-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30, verbose_name='Carusel name')),
                ('name2', models.CharField(max_length=60, verbose_name='Carusel name')),
                ('about', models.TextField(verbose_name='Carusel about')),
                ('img1', models.ImageField(upload_to='media', verbose_name='Carusel image')),
                ('img2', models.ImageField(upload_to='media', verbose_name='Carusel image')),
            ],
            options={
                'verbose_name': 'HomeCarusel',
                'verbose_name_plural': 'HomeCarusels',
            },
        ),
    ]
