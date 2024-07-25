from rest_framework import serializers
from .models import Position, Country, City, Region, Neighborhood, Employee, Test, Question, Answer


class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'text_content']


class ImageQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'image_content']


class VideoQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'video_content']


class DynamicQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title']

    def to_representation(self, instance):
        if instance.content_type == 'text':
            return TextQuestionSerializer(instance).data
        elif instance.content_type == 'image':
            return ImageQuestionSerializer(instance).data
        elif instance.content_type == 'video':
            return VideoQuestionSerializer(instance).data
        else:
            return super().to_representation(instance)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title']


class TextAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ['title', 'question', 'text_content']


class ImageAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ['title', 'question', 'image_content']


class DynamicAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['title']

    def to_representation(self, instance):
        if instance.content_type == 'text':
            return TextAnswerSerializer(instance).data
        elif instance.content_type == 'image':
            return ImageAnswerSerializer(instance).data
        else:
            return super().to_representation(instance)


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
        fields = ('id',
                  'full_name',
                  'position',
                  'country',
                  'city',
                  'region',
                  'neighborhood'
                  )


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id',
                  'title',
                  'question',
                  'answer',
                  'employee',
                  'balls'
                  )


class BallsSumSerializer(serializers.Serializer):
    total_balls = serializers.IntegerField()


class TotalBallsSerializer(serializers.Serializer):
    total_balls = serializers.IntegerField()
