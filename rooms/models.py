from django.db import models
from common.models import CommonModel


# Room Definition
class Room(CommonModel):
    class RoomKindOptions(models.TextChoices):
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

    # Name of the room
    name = models.CharField(
        max_length=128,
        default="",
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

    # Room Kind
    kind = models.CharField(
        max_length=128,
        choices=RoomKindOptions.choices,
        null=True,
    )

    # Category
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        # related_name="rooms",
    )

    # Owner
    # One room have to have one owner, but one onwer can have many rooms.
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        # related_name="rooms",
    )

    # Amenity
    # One room can have different amenity,
    # some room have 1 amenity but different room cam have 7 at the same time.
    amenity = models.ManyToManyField(
        "rooms.Amenity",
        # related_name="rooms",
    )

    def __str__(self):
        return self.name

    def total_amenities(self):
        return self.amenity.count()

    def average_rate(self):
        reviews = self.review_set.all()
        if not reviews:
            return "No Review"
        return round(
            sum([r["rating"] for r in reviews.values("rating")]) / len(reviews), 1
        )


# Amenity Definition
class Amenity(CommonModel):
    class Meta:
        verbose_name_plural = "Amenities"

    name = models.CharField(
        max_length=128,
    )
    description = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
