# Generated by Django 4.2.7 on 2023-12-16 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("posts", "0009_remove_posts_user_posts_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="user_name",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usernames",
                to="user.user",
            ),
        ),
    ]