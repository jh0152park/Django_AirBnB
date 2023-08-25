from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    class CategoryKindOption(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = ("expreriences", "Expreriences")

    # Name of the category
    name = models.CharField(
        max_length=32,
    )

    # Kind
    kind = models.CharField(
        max_length=32,
        choices=CategoryKindOption.choices,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
