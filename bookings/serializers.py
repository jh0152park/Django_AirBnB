from datetime import datetime

from django.utils import timezone

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import DateField
from rest_framework.serializers import ValidationError
from rest_framework.serializers import SerializerMethodField

from .models import Booking
from rooms.serializers import SimpleRoomSerializer
from experiences.serializers import SimpleExperienceSerializer


class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in_date",
            "check_out_date",
            "experience_time",
            "guests",
            "room",
            "experience",
        )

    room = SimpleRoomSerializer()
    experience = SimpleExperienceSerializer()


class TestReservationSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        # fields = (
        #     # "user",
        #     "check_in_date",
        #     "check_out_date",
        #     "guests",
        # )


class TestSerializer(ModelSerializer):
    room = SimpleRoomSerializer()
    reservations = SerializerMethodField()

    class Meta:
        model = Booking
        fields = (
            "room",
            "reservations",
        )


class ExperienceBookingListSerializer(ModelSerializer):
    class Meta:
        model = Booking
        exclude = (
            "created_at",
            "updated_at",
            "category",
            "check_in_date",
            "check_out_date",
            "room",
            "experience",
        )


class CreateExperienceBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "experience_time",
            "guests",
            "user",
        )

    def validate_experience_time(self, value):
        now = timezone.localtime(timezone.now())
        print(f"input value is {value}")
        print(f"now is {now}")
        print(f"type is {type(value)} and {type(now)}")
        if now > value:
            raise ValidationError(
                "Can't reservation due to experience time isn't future!"
            )

        return value


class CreateRoomBookingSerializer(ModelSerializer):
    check_in_date = DateField()
    check_out_date = DateField()

    class Meta:
        model = Booking
        # recieved datas from user
        fields = (
            "check_in_date",
            "check_out_date",
            "guests",
        )

    def validate_check_in_date(self, value):
        now = timezone.localtime(timezone.now()).date()

        if now > value:
            raise ValidationError(
                "Can't reservation due to check in date isn't future!"
            )

        return value

    def validate_check_out_date(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise ValidationError(
                "Can't reservation due to check out date isn't future!"
            )

        return value

    def validate(self, data):
        room = self.context.get("room")

        if data["check_in_date"] >= data["check_out_date"]:
            raise ValidationError(
                "Check out data is looks like smaller than check in date."
            )

        if Booking.objects.filter(
            room=room,
            check_in_date__lte=data["check_out_date"],
            check_out_date__gte=data["check_in_date"],
        ).exists():
            raise ValidationError(
                "Already has bookings between check in and check out date"
            )

        return data


class ExperienceBookingDetailSerializer(ModelSerializer):
    class Meta:
        model = Booking
        # fields = "__all__"
        exclude = (
            "created_at",
            "updated_at",
            "category",
            "user",
        )
