import strawberry
from . import models


@strawberry.django.type(models.Room)
class RoomType:
    name: strawberry.auto
    kind: strawberry.auto
    country: strawberry.auto
    city: strawberry.auto
