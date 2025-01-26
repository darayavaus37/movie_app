from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserConfirmation  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        from .models import UserConfirmation  
        user = User.objects.create_user(**validated_data)
        UserConfirmation.objects.create(user=user)
        return user

class UserConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfirmation
        fields = ['confirmation_code', 'is_confirmed']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Director  
        model = Director
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Movie  
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Review  
        model = Review
        fields = ['id', 'text', 'stars', 'movie']
