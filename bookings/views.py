from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import ParseError
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import PublicBookingSerializer
from .serializers import TestSerializer

from rooms.models import Room
from users.models import User

import json
from datetime import datetime


class MyReservation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        my_booking = Booking.objects.filter(user=user)

        for b in my_booking:
            print(b.room)
            print(b.experience)

        seriailizer = PublicBookingSerializer(
            my_booking,
            many=True,
        )
        return Response(seriailizer.data)


class MyRoomReservation(MyReservation):
    permission_classes = [IsAuthenticated]

    def get(self, request, host_id):
        if not request.user.is_host:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        my_rooms_bookings = []
        # host_id == request.user.is_host

        host = User.objects.filter(username=host_id)
        rooms = Room.objects.filter(owner=request.user)

        for room in rooms:
            bookings = room.booking_set.all()
            print(f"room name is: {room}")
            if len(bookings) > 0 and room.name not in my_rooms_bookings:
                my_rooms_bookings.append(
                    {
                        # "room": room,
                        "room": room.name,
                        "reservations": [],
                    },
                )
                # my_rooms_bookings[room.name] = {
                #     "reserved": [],
                # }

            for book in bookings:
                """
                my_rooms_bookings[room.name]["reserved"].append(
                    {
                        "user": book.user.username,
                        "guests": book.guests,
                        "check_in": book.check_in_date.strftime("%Y-%m-%d"),
                        "check_out": book.check_out_date.strftime("%Y-%m-%d"),
                    }
                )
                """
                my_rooms_bookings[-1]["reservations"].append(
                    {
                        "user": book.user.username,
                        "guests": book.guests,
                        "check_in": book.check_in_date.strftime("%Y-%m-%d"),
                        "check_out": book.check_out_date.strftime("%Y-%m-%d"),
                        # "user": book.user,
                        # "check_in_date": book.check_in_date,
                        # "check_out_date": book.check_out_date,
                    }
                )

        print(my_rooms_bookings)

        if len(my_rooms_bookings) == 0:
            return Response({"reservation": False})
        return Response({"reservation": json.dumps(my_rooms_bookings)})
        # return Response({"ok": False})
        # return Response(serializer.data)
