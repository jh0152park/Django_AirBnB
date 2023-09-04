from django.db import transaction
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import ParseError
from rest_framework.exceptions import PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Room
from .models import Amenity
from .serializers import AmenitySerializer
from .serializers import RoomListSerializer
from .serializers import RoomDetailsSerializer

from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer
from categories.models import Category
from medias.serializers import PhotoSerializer
from reviews.serializers import ReviewSerializer


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
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenitry = self.get_object(pk)
        amenitry.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(
            all_rooms,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomDetailsSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required.")

            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindOption.EXPERIENCES:
                    raise ParseError("Category kind is should be rooms.")
            except Category.DoesNotExist:
                raise ParseError("Category not exist.")

            try:
                with transaction.atomic():
                    room = serializer.save(
                        owner=request.user,
                        category=category,
                    )
                    amenities = request.data.get("amenities")

                    for amenity_pk in amenities:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        room.amenity.add(amenity)
                    serializer = RoomDetailsSerializer(room)

                    return Response(serializer.data)
            except Exception:
                raise ParseError("Amenity not found.")
        else:
            return Response(serializer.errors)


class RoomDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailsSerializer(
            room,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)

        if request.user != room.owner:
            raise PermissionDenied

        serializer = RoomDetailsSerializer(
            room,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            category_pk = request.data.get("category")

            if not category_pk:
                raise ParseError("Category is required.")

            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindOption.EXPERIENCES:
                    raise ParseError("Category kind is should be rooms.")
            except Category.DoesNotExist:
                raise ParseError("Category not exist.")

            try:
                with transaction.atomic():
                    room = serializer.save(
                        owner=request.user,
                        category=category,
                    )
                    amenities = request.data.get("amenities")
                    for amenity_pk in amenities:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        room.amenity.add(amenity)

                    serializer = RoomDetailsSerializer(room)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Amenity not found.")

        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)

        if request.user != room.owner:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class RoomReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        item = 5
        start = (page - 1) * item
        converter = ReviewSerializer(
            room.review_set.all()[start : start + item],
            many=True,
        )
        return Response(converter.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                room=self.get_object(pk),
                user=request.user,
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            raise NotFound


class RoomAmenites(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        item = 5
        start = (page - 1) * item
        converter = AmenitySerializer(
            room.amenity.all()[start : start + item],
            many=True,
        )
        return Response(converter.data)


class RoomPhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        room = self.get_object(pk)

        if room.owner != request.user:
            raise PermissionDenied

        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(room=room)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RoomBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        now = timezone.now()
        local_time = timezone.localtime(now).date()

        room = self.get_object(pk)
        bookings = Booking.objects.filter(
            room=room,
            category=Booking.BookingOption.ROOM,
            check_in_date__gt=local_time,
        )
        serializer = PublicBookingSerializer(
            bookings,
            many=True,
        )
        return Response(serializer.data)
