from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def see_all_room(request):
    return HttpResponse("see all rooms")


def see_one_room(request, room_id):
    return HttpResponse(f"room id is {room_id}")
