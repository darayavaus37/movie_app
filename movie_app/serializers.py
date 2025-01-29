from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Review, Director, UserConfirmation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        from .models import UserConfirmation
        UserConfirmation.objects.create(user=user)
        return user


class UserConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'movie_app.UserConfirmation'
        fields = ['confirmation_code', 'is_confirmed']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'movie_app.Director'  
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'movie_app.Movie'  
        fields = ['id', 'title', 'director', 'description', 'release_date', 'duration']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'movie_app.Review'  
        fields = ['id', 'movie', 'text', 'stars', 'created_at']


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    bio = serializers.CharField(allow_blank=True, required=False)

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must contain only letters.")
        return value
