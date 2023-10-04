import strawberry

from . import models
from users.types import UserType


@strawberry.django.type(models.Room)
class RoomType:
    name: strawberry.auto
    kind: strawberry.auto
    country: strawberry.auto
    city: strawberry.auto
    owner: "UserType"
