# Generated by Django 4.2.4 on 2023-09-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.URLField(blank=True, null=True),
        ),
    ]
