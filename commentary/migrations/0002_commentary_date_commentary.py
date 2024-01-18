# Generated by Django 4.2.7 on 2024-01-13 06:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("commentary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentary",
            name="date_commentary",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
