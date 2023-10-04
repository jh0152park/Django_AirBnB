import strawberry
import typing

from strawberry.types import Info

from . import models
from users.types import UserType
from reviews.types import ReviewType
from wishlists.models import Wishlist


@strawberry.django.type(models.Room)
class RoomType:
    name: strawberry.auto
    kind: strawberry.auto
    country: strawberry.auto
    city: strawberry.auto
    owner: "UserType"

    @strawberry.field
    def rate(self) -> float:
        return self.average_rate()

    @strawberry.field
    def review(self, page: int) -> typing.List["ReviewType"]:
        if page < 0:
            page = 1

        item = 5
        start = (page - 1) * item
        end = item + start

        return self.review_set.all()[start:end]

    @strawberry.field
    def is_owner(self, info: Info) -> bool:
        return self.owner == info.context.request.user

    @strawberry.field
    def is_liked(self, info: Info) -> bool:
        return Wishlist.objects.filter(
            user=info.context.request.user,
            rooms__pk=self.pk,
        ).exists()
