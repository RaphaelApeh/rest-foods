# Generated by Django 5.1.4 on 2025-02-08 18:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
