from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from .models import Amenity
from .models import Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "pk",
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
    is_liked = SerializerMethodField()
    photo_set = PhotoSerializer(
        many=True,
        read_only=True,
    )
    review_count = SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_room_rate(self, room):
        return room.average_rate()

    def get_is_owner(self, room):
        request = self.context.get("request")
        if request:
            return room.owner == request.user
        # return False

    def get_is_liked(self, room):
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    user=request.user,
                    rooms__pk=room.pk,
                ).exists()
        # return False

    def get_review_count(self, room):
        return room.get_review_count()


class SimpleRoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ("name",)
