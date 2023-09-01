from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from .models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
