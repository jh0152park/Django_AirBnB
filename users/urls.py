from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import Me
from .views import LogIn
from .views import LogOut
from .views import Users
from .views import PublicUser
from .views import changePassword
from .views import JWTLogIn
from .views import GithubLogIn
from .views import KakaoLogIn

urlpatterns = [
    path("", Users.as_view()),
    path("me", Me.as_view()),
    path("change-password", changePassword.as_view()),
    path("log-in", LogIn.as_view()),
    path("log-out", LogOut.as_view()),
    path("token-login", obtain_auth_token),
    path("jwt-login", JWTLogIn.as_view()),
    path("@<str:username>", PublicUser.as_view()),
    path("github", GithubLogIn.as_view()),
    path("kakao", KakaoLogIn.as_view()),
]
