# Generated by Django 4.2.1 on 2023-06-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bands", "0004_rename_image_band_image_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="source",
            field=models.URLField(default=""),
        ),
    ]