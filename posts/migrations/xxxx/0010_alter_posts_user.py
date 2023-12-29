# Generated by Django 4.2.7 on 2023-12-15 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("posts", "0009_alter_posts_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.user"
            ),
        ),
    ]