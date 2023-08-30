from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True,
        max_length=32,
    )
    kind = serializers.ChoiceField(
        # max_length=32,
        choices=Category.CategoryKindOption.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
