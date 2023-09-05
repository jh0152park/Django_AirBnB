from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import TimeField


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
    # perks = PerkSerializer(
    #     read_only=True,
    #     many=True,
    # )

    # start = TimeField()
    # end = TimeField()

    class Meta:
        model = Experience
        # fields = "__all__"
        exclude = (
            "created_at",
            "updated_at",
            # "address",
            # "start",
            # "end",
            # "description",
            # "host",
            "category",
        )

    def validate(self, attrs):
        print("###############")
        print(attrs)
        print("###############")
        return attrs
