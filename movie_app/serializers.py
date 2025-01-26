from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movie_count')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')


class ReviewValiditySerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'average_rating')

    def get_average_rating(self, movie):
        reviews = movie.review_set.all()
        if reviews:
            sum_reviews = sum([review.stars for review in reviews])
            average = sum_reviews / len(reviews)  # 6/2 = 3
            return average
        return None


class MovieValidirySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField()

