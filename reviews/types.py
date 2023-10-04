import strawberry
from . import models


@strawberry.django.type(models.Review)
class ReviewType:
    id: strawberry.auto
    review: strawberry.auto
    rating: strawberry.auto
