# Generated by Django 5.1.4 on 2025-01-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="images"),
        ),
        migrations.AddField(
            model_name="food",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
