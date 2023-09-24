# Generated by Django 4.2.4 on 2023-09-23 12:50

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_video_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.FileField(
                default="/home/sebi/Code/CS50W/Final Project/youtv/static/avatar.png",
                storage=django.core.files.storage.FileSystemStorage(
                    location="/home/sebi/Code/CS50W/Final Project/youtv/media/avatars"
                ),
                upload_to="avatars/",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="/home/sebi/Code/CS50W/Final Project/youtv/media/videos"
                ),
                upload_to="videos/",
            ),
        ),
    ]
