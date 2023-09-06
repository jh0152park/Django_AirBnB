from django.urls import path

from .views import Perks
from .views import PerkDetails
from .views import Experiencies
from .views import ExperienceDetail
from .views import ExperienceBookingLists

urlpatterns = [
    path("", Experiencies.as_view()),
    path("<int:pk>", ExperienceDetail.as_view()),
    path("<int:pk>/bookings/", ExperienceBookingLists.as_view()),
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetails.as_view()),
]
