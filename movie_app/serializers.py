from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField
    class Meta:
        model = Director
        fields = ("id", "name", "movie_count")
    
    def get_movie_count(self, director):
        return director.movie.count()

    


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField
    class Meta:
        model = Movie
        fields = ("id", "titile", "description", "duration", "director", "reviews", "average_rating")


class ReviewSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField
    class Meta:
        model = Review
        fields = ("id", "text", "movie", "stars")
        def set_average_rating(self, movie):
            reviews = movie.reviews.all()
            if reviews:
                sum_reviews = sum([reviews.stars for review in reviews])
                average = sum_reviews/len(reviews)
                return average
            return None







