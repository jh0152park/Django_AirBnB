from django.utils import timezone

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import DateField
from rest_framework.serializers import ValidationError

from .models import Booking


class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in_date",
            "check_out_date",
            "experience_time",
            "guests",
        )


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
