# Generated by Django 4.2.4 on 2023-08-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_rename_profile_pciture_user_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
