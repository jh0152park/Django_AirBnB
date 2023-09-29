from django.urls import path
from . import views

urlpatterns = [
    path("", views.MyReservation.as_view()),
    path("<str:host_id>", views.MyRoomReservation.as_view()),
]
