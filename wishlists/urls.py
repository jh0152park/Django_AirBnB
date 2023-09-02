from django.urls import path
from .views import Wishlists
from .views import WishlistDetail

urlpatterns = [
    path("", Wishlists.as_view()),
    path("<int:pk>", WishlistDetail.as_view()),
]
