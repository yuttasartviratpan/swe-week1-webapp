# Generated by Django 4.1.6 on 2023-02-07 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendingMachine", "0005_alter_item_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 7, 18, 42, 24, 440283)
            ),
        ),
    ]
