# Generated by Django 4.2.7 on 2023-12-28 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("posts", "0008_rename_user_code_posts_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="posts",
            name="user",
        ),
        migrations.AddField(
            model_name="posts",
            name="user_name",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usernames",
                to="user.user",
            ),
        ),
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
