# Generated by Django 4.2.7 on 2023-12-14 00:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_alter_posts_user_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="posts",
            old_name="user_code",
            new_name="user",
        ),
    ]
