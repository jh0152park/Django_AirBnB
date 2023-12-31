# Generated by Django 4.2.4 on 2023-08-25 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=128, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "Amenities",
            },
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(default="", max_length=128)),
                ("country", models.CharField(default="South Korea", max_length=64)),
                ("city", models.CharField(default="Seoul", max_length=128)),
                ("price", models.PositiveIntegerField()),
                ("rooms", models.PositiveIntegerField()),
                ("toilets", models.PositiveIntegerField()),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=256)),
                ("pet_allow", models.BooleanField(default=False)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("entire_place", "Entire Place"),
                            ("private_rooms", "Private Room"),
                            ("shared_rooms", "Shared Room"),
                        ],
                        max_length=128,
                        null=True,
                    ),
                ),
                ("amenity", models.ManyToManyField(to="rooms.amenity")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="categories.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
