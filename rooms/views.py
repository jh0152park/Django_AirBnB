from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


# Create your views here.
def see_all_room(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
            "title": "See All Rooms here!",
        },
    )


def see_one_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        return render(
            request,
            "room_detail.html",
            {"room": room},
        )
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {"not_found": True},
        )
