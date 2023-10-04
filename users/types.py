import strawberry
from . import models


@strawberry.django.type(models.User)
class UserType:
    name: strawberry.auto
    email: strawberry.auto
    username: strawberry.auto
