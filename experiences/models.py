from django.db import models
from common.models import CommonModel


# Create your models here.
class Experience(CommonModel):
    # Location
    country = models.CharField(
        max_length=64,
        default="South Korea",
    )
    city = models.CharField(
        max_length=128,
        default="Seoul",
    )

    # Name
    name = models.CharField(
        max_length=128,
    )

    # Host
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    # Price
    price = models.PositiveIntegerField()

    # Address
    address = models.CharField(
        max_length=128,
    )

    # Times
    start = models.TimeField()
    end = models.TimeField()

    # Description
    description = models.TextField()

    # Perks, what we can do with is experience program
    perks = models.ManyToManyField(
        "experiences.Perk",
    )

    # Category
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    name = models.CharField(
        max_length=64,
    )
    detail = models.CharField(
        max_length=128,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name


"""
{
    "country": "South Korea",
    "city": "Seoul",
    "name": "Watch movie",
    "price":132,
    "address":"123",
    "start": "13:00",
    "end": "17:00",
    "description":"literally watching movie",
    "host": 1,
    "perks": [3,4]
}
"""
