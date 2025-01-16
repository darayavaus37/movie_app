from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255, min_length=2)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=255, min_length=1)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(min_value=1, required=True)
    director_id = serializers.IntegerField(required=True)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError("Director does not exist!")
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=1000, min_length=5)
    movie_id = serializers.IntegerField(required=True)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=True)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError("Movie does not exist!")
        return movie_id




