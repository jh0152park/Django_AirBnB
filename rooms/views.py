from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


# Create your views here.
def see_all_room(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {"rooms": rooms},
    )


def see_one_room(request, room_id):
    return HttpResponse(f"room id is {room_id}")
