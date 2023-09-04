from django.urls import path

from .views import Me
from .views import LogIn
from .views import LogOut
from .views import Users
from .views import PublicUser
from .views import changePassword

urlpatterns = [
    path("", Users.as_view()),
    path("me", Me.as_view()),
    path("change-password", changePassword.as_view()),
    path("log-in", LogIn.as_view()),
    path("log-out", LogOut.as_view()),
    path("@<str:username>", PublicUser.as_view()),
]
