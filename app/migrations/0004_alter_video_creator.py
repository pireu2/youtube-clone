# Generated by Django 4.2.4 on 2023-09-21 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_video_creator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="uploads",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
