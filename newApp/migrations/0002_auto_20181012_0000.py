# Generated by Django 2.1.2 on 2018-10-11 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 0, 0, 10, 969951)),
        ),
    ]