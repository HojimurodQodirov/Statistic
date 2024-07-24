from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Position, Country, City, Region, Neighborhood, Employee, Test
from .serializers import PositionSerializer, CountrySerializer, CitySerializer, RegionSerializer, \
    NeighborhoodSerializer, EmployeeSerializer, TestSerializer, TotalBallsSerializer
from .filters import EmployeeFilter


class PositionList(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class RegionList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class NeighborhoodList(generics.ListAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter


class EmployeeListProcent(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter

    def get(self, request, *args, **kwargs):
        employees = self.filter_queryset(self.get_queryset())

        total_balls_sum = Test.objects.filter(employee__in=employees).aggregate(Sum('balls'))
        total_balls_value = total_balls_sum['balls__sum'] if total_balls_sum['balls__sum'] is not None else 0

        total_employees_count = employees.count()
        max_balls = total_employees_count * 200

        if max_balls > 0:
            percent = (total_balls_value / max_balls) * 100
            rounded_percent = round(percent, 1)
        else:
            rounded_percent = 0.0

        response_data = {
            'procent': rounded_percent
        }

        return Response(response_data)


class TestList(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer




