from django.urls import path

from .views import Me
from .views import Users

urlpatterns = [
    path("", Users.as_view()),
    path("me", Me.as_view()),
]
