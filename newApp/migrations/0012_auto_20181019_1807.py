# Generated by Django 2.1.2 on 2018-10-19 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0011_auto_20181019_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidauction',
            name='bid',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 22, 18, 7, 36, 620805)),
        ),
        migrations.AlterField(
            model_name='bidauction',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 18, 7, 36, 621805)),
        ),
    ]
