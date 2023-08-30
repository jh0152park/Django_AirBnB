from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.CharField(
        max_length=16,
    )
