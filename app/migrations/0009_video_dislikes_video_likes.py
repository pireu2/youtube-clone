# Generated by Django 4.2.4 on 2023-09-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_user_subscribers"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="dislikes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="video",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]
