# Generated by Django 3.1.2 on 2021-03-15 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_auto_20210313_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 15, 20, 45, 506829, tzinfo=utc)),
        ),
    ]