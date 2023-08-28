from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zeoo")
def reset_prices(model_admin, request, queryset):
    for room in queryset.all():
        room.price = 0
        room.save()
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = (
        "name",
        "owner",
        "price",
        "total_amenities",
        "average_rate",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "city",
        "country",
        "pet_allow",
        "amenity",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "price",
        "owner__username",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
