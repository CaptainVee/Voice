# Generated by Django 3.1.2 on 2021-02-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20210218_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]