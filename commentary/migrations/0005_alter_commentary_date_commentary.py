# Generated by Django 4.2.7 on 2024-01-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commentary", "0004_alter_commentary_date_commentary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="date_commentary",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
