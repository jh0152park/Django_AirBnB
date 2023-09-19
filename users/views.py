import jwt
import requests

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import PrivateUserSerializer

from users.models import User


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            raise Response(serializer.errors)


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        serializer = PrivateUserSerializer(data=request.data)

        if not password:
            raise exceptions.ParseError

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PublicUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except user.DoesNotExist:
            raise exceptions.NotFound
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)


class changePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise exceptions.ParseError

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise exceptions.ParseError


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise exceptions.ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"login_success": True}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"login_success": False}, status=status.HTTP_400_BAD_REQUEST
            )


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class JWTLogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise exceptions.ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            token = jwt.encode(
                {
                    "pk": user.pk,
                },
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response({"token": token})
        else:
            return Response({"error": "Invalid username or password"})


class GithubLogIn(APIView):
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                f"https://github.com/login/oauth/access_token?code={code}&client_id=bf19cc5900af3a5bca3c&client_secret={settings.GITHUB_CLIENT_SECRET_KEY}",
                headers={
                    "Accept": "application/json",
                },
            )
            access_token = access_token.json().get("access_token")

            user_data = requests.get(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_data = user_data.json()
            print(user_data)

            user_email = requests.get(
                "https://api.github.com/user/emails",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_email = user_email.json()
            print(len(user_email))
            print(type(user_email))
            print(f"\nuser_email: {user_email}\n")
            try:
                user = User.objects.get(email=user_email[0]["email"])
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            # try to create a new account
            except User.DoesNotExist:
                user = User.objects.create(
                    username=user_data["login"],
                    name=user_data["name"],
                    email=user_email[0]["email"],
                    profile_picture=user_data["avatar_url"],
                )
                user.set_unusable_password()
                user.save()
                login(request, user)
                return Response(status=status.HTTP_200_OK)

        except Exception as error:
            print(f"occurred error as below\n{error}")
            return Response(status=status.HTTP_400_BAD_REQUEST)


class KakaoLogIn(APIView):
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                "https://kauth.kakao.com/oauth/token",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                data={
                    "grant_type": "authorization_code",
                    "client_id": "fcb3b6ccc19cc01f2fe6aa6bf4cf63dc",
                    "redirect_uri": "http://127.0.0.1:3000/social/kakao",
                    "code": code,
                },
            )
            access_token = access_token.json()["access_token"]
            user_data = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            )
            user_data = user_data.json()
            for k in user_data.keys():
                print(k)
                print(user_data[k])
                print("\n")

            kakao_account = user_data["kakao_account"]
            profile = kakao_account["profile"]

            try:
                user = User.objects.get(email=kakao_account["email"])
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User.objects.create(
                    email=kakao_account["email"],
                    username=profile["nickname"],
                    name=profile["nickname"],
                    profile_picture=profile["profile_image_url"],
                )
                user.set_unusable_password()
                user.save()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception as error:
            print(f"occured exception error as below\n{error}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
