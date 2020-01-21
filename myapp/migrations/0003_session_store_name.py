# Generated by Django 3.0.2 on 2020-01-20 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_inventory_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='store_name',
            field=models.CharField(default=datetime.datetime(2020, 1, 20, 19, 11, 47, 548096, tzinfo=utc), max_length=50, unique=True),
            preserve_default=False,
        ),
    ]