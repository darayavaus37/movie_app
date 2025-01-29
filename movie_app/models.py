from django.db import models
from django.contrib.auth.models import User
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction




STARS = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
)



from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import UserConfirmation 
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






        
 