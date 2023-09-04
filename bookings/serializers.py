from rest_framework.serializers import ModelSerializer

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
