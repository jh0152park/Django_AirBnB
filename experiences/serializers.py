from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import TimeField
from rest_framework.serializers import SerializerMethodField


from .models import Perk
from .models import Experience


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        # fields = "__all__"
        exclude = (
            # "id",
            "created_at",
            "updated_at",
        )


class PerkNameSerializer(ModelSerializer):
    class Meta:
        model = Perk
        exclude = (
            "created_at",
            "updated_at",
        )


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        # fields = "__all__"
        exclude = (
            "created_at",
            "updated_at",
            "category",
        )


class ExperienceDetailSerializer(ModelSerializer):
    # perks = PerkNameSerializer(
    #     read_only=True,
    #     many=True,
    # )

    class Meta:
        model = Experience
        exclude = (
            "created_at",
            "updated_at",
            "category",
        )


class SimpleExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = ("name",)
