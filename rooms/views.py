from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Room


class Amenities(APIView):
    def get(self, requset):
        pass

    def post(self, requset):
        pass


class AmenityDetail(APIView):
    def get(self, requset, pk):
        pass

    def put(self, requset, pk):
        pass

    def delete(self, requset, pk):
        pass


# Create your views here.
# def see_all_room(request):
#     rooms = Room.objects.all()
#     return render(
#         request,
#         "all_rooms.html",
#         {
#             "rooms": rooms,
#             "title": "See All Rooms here!",
#         },
#     )


# def see_one_room(request, room_id):
#     try:
#         room = Room.objects.get(pk=room_id)
#         return render(
#             request,
#             "room_detail.html",
#             {"room": room},
#         )
#     except Room.DoesNotExist:
#         return render(
#             request,
#             "room_detail.html",
#             {"not_found": True},
#         )
