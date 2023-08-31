# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Room
from .models import Amenity
from .serializers import AmenitySerializer
from .serializers import RoomListSerializer


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(
                AmenitySerializer(amenity).data,
            )
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenitry = self.get_object(pk)
        serializer = AmenitySerializer(amenitry)

        return Response(
            serializer.data,
        )

    def put(self, request, pk):
        amenitry = self.get_object(pk)
        serializer = AmenitySerializer(
            amenitry,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            update_amenity = serializer.save()
            return Response(
                AmenitySerializer(update_amenity).data,
            )
        else:
            return Response(serial.errors)

    def delete(self, request, pk):
        amenitry = self.get_object(pk)
        amenitry.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)


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
