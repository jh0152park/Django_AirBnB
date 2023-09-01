from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from .models import Amenity
from .models import Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "name",
            "country",
            "city",
            "price",
            "pk",
            "room_rate",
            "is_owner",
            "photo_set",
        )

    room_rate = SerializerMethodField()
    is_owner = SerializerMethodField()
    photo_set = PhotoSerializer(
        many=True,
        read_only=True,
    )

    def get_room_rate(self, room):
        return room.average_rate()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


class RoomDetailsSerializer(ModelSerializer):
    owner = TinyUserSerializer(
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    amenity = AmenitySerializer(
        many=True,
        read_only=True,
    )
    room_rate = SerializerMethodField()
    is_owner = SerializerMethodField()
    photo_set = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = "__all__"

    def get_room_rate(self, room):
        return room.average_rate()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user
