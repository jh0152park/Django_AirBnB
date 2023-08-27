from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdming(admin.ModelAdmin):
    list_display = (
        "category",
        "user",
        "room",
        "experience",
        "check_in_date",
        "check_out_date",
        "experience_time",
        "guests",
    )

    list_filter = ("category",)
