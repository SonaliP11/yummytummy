# Generated by Django 5.1.5 on 2025-02-05 23:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChefProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('bio', models.TextField()),
                ('chef_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='chef_image')),
                ('interests', models.CharField(max_length=100)),
            ],
        ),
    ]
