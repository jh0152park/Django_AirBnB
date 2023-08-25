from django.db import models
from common.models import CommonModel


# Room Definition
class Room(CommonModel):
    class RoomCategoryOptions(models.TextChoices):
        ENTIRE_PLACE = (
            "entire_place",
            "Entire Place",
        )
        PRIVATE_ROOM = (
            "private_rooms",
            "Private Room",
        )
        SHARED_ROOM = (
            "shared_rooms",
            "Shared Room",
        )

    # Location
    country = models.CharField(
        max_length=64,
        default="South Korea",
    )
    city = models.CharField(
        max_length=128,
        default="Seoul",
    )

    # Price
    price = models.PositiveIntegerField()

    # Number of Rooms
    rooms = models.PositiveIntegerField()

    # Number of Toilets
    toilets = models.PositiveIntegerField()

    # Description of House
    description = models.TextField()

    # Address of House
    address = models.CharField(
        max_length=256,
    )

    # Pets Allow
    pet_allow = models.BooleanField(
        default=False,
    )

    # Category
    category = models.CharField(
        max_length=128,
        choices=RoomCategoryOptions.choices,
    )

    # Owner
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    # Amenity
    amenity = models.ManyToManyField(
        "rooms.Amenity",
    )


# Amenity Definition
class Amenity(CommonModel):
    name = models.CharField(
        max_length=128,
    )
    description = models.CharField(
        max_length=128,
        default="",
        null=True,
    )
