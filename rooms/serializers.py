from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from .models import Amenity
from .models import Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


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
        )

    room_rate = SerializerMethodField()

    def get_room_rate(self, room):
        return room.average_rate()


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

    class Meta:
        model = Room
        fields = "__all__"

    def get_room_rate(self, room):
        return room.average_rate()
