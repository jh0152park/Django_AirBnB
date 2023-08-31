from rest_framework.serializers import ModelSerializer

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
        )


class RoomDetailsSerializer(ModelSerializer):
    owner = TinyUserSerializer()
    category = CategorySerializer()
    amenity = AmenitySerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"
