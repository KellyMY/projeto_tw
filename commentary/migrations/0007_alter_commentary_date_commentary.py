# Generated by Django 4.2.7 on 2024-01-14 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commentary", "0006_alter_commentary_date_commentary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="date_commentary",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 14, 9, 55, 30, 600809)
            ),
        ),
    ]
