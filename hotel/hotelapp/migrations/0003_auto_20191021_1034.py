# Generated by Django 2.2.6 on 2019-10-21 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_auto_20191019_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='log_in',
            field=models.DateField(default=datetime.date(2019, 10, 21)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='log_out',
            field=models.DateField(default=datetime.date(2019, 10, 22)),
        ),
    ]