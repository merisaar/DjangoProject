# Generated by Django 2.1.2 on 2018-10-18 08:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0002_auto_20181018_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionbid',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='auctionbid',
            name='bidder',
        ),
        migrations.AddField(
            model_name='auction',
            name='bidder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 21, 11, 39, 42, 604432)),
        ),
        migrations.DeleteModel(
            name='AuctionBid',
        ),
    ]
