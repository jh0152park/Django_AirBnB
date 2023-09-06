from django.utils import timezone

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Perk
from .models import Experience
from .serializers import PerkSerializer
from .serializers import ExperienceSerializer
from .serializers import ExperienceDetailSerializer

from bookings.models import Booking
from bookings.serializers import ExperienceBookingListSerializer


class Experiencies(APIView):
    def get(self, request):
        experiencies = Experience.objects.all()
        serializer = ExperienceSerializer(
            experiencies,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            experience = serializer.save()
            serializer = ExperienceSerializer(experience)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ExperienceDetail(APIView):
    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
            experience,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        experience = self.get_object(pk)
        rawdata = ExperienceDetailSerializer(
            experience,
            data=request.data,
            partial=True,
        )
        if rawdata.is_valid():
            data = rawdata.save()

            update_perks = request.data.get("perks")
            for perk in update_perks:
                data.perks.add(Perk.objects.get(pk=perk))

            convert = ExperienceDetailSerializer(data)
            return Response(convert.data)
        else:
            return Response(rawdata.errors)

    def delete(self, request, pk):
        experience = self.get_object(pk)
        experience.delete()
        return Response(status=status.HTTP_200_OK)


class Perks(APIView):
    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serializer.errors)


class PerkDetails(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(
            perk,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_perk = serializer.save()
            return Response(
                PerkSerializer(update_perk).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExperienceBookingLists(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        now = timezone.now()
        local_time = timezone.localtime(now).date()
        experience = self.get_object(pk)

        bookings = Booking.objects.filter(
            experience=experience,
            category=Booking.BookingOption.EXPERIENCE,
            experience_time__gt=local_time,
        )
        serializer = ExperienceBookingListSerializer(
            bookings,
            many=True,
        )
        return Response(serializer.data)
