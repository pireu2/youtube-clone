# Generated by Django 4.2.4 on 2023-09-24 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0011_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 24, 19, 18, 1, 849212)
            ),
        ),
    ]
