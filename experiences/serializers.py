from rest_framework.serializers import ModelSerializer

from .models import Perk
from .models import Experience


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        # fields = "__all__"
        exclude = (
            "created_at",
            "updated_at",
        )


class ExperienceSerializer(ModelSerializer):
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Experience
        fields = "__all__"
