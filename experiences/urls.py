from django.urls import path
from .views import Perks
from .views import PerkDetails

urlpatterns = [
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetails.as_view()),
]
