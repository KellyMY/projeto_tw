# Generated by Django 4.2.7 on 2023-12-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0011_alter_posts_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="description",
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name="posts",
            name="title",
            field=models.CharField(max_length=1500),
        ),
    ]