# Generated by Django 3.1.2 on 2021-02-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_announcement_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
