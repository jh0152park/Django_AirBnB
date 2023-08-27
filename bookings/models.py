from django.db import models
from common.models import CommonModel


class Booking(CommonModel):
    class BookingOption(models.TextChoices):
        ROOM = (
            "room",
            "Room",
        )
        EXPERIENCE = (
            "experience",
            "Experience",
        )

    category = models.CharField(
        max_length=32,
        choices=BookingOption.choices,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    check_in_date = models.DateField(
        null=True,
        blank=True,
    )

    check_out_date = models.DateField(
        null=True,
        blank=True,
    )

    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    guests = models.PositiveIntegerField(
        default=1,
    )

    def __str__(self):
        return f"{self.category.title()} booking for {self.user}"
