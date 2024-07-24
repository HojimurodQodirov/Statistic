from rest_framework import serializers
from .models import Position, Country, City, Region, Neighborhood, Employee, Test


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ['title']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['title']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['title']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['title']


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ['title']


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    country = CountrySerializer()
    city = CitySerializer()
    region = RegionSerializer()
    neighborhood = NeighborhoodSerializer()

    class Meta:
        model = Employee
        fields = ['id',
                  'full_name',
                  'position',
                  'country',
                  'city',
                  'region',
                  'neighborhood']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id',
                  'title',
                  'question',
                  'answer',
                  'employee',
                  'balls']


class BallsSumSerializer(serializers.Serializer):
    total_balls = serializers.IntegerField()


class TotalBallsSerializer(serializers.Serializer):
    total_balls = serializers.IntegerField()
