# Generated by Django 4.2.4 on 2023-08-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiences", "0002_initial"),
        ("rooms", "0002_initial"),
        ("wishlists", "0002_rename_owner_wishlist_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ManyToManyField(blank=True, to="experiences.experience"),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ManyToManyField(blank=True, to="rooms.room"),
        ),
    ]
