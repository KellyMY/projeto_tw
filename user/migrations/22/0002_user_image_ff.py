# Generated by Django 4.2.7 on 2024-01-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.FileField(default="", upload_to="img"),
            preserve_default=False,
        ),
    ]
