from django.db import models
from django.contrib.auth.models import User
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .serializers import DirectorSerializer,MovieSerializer,ReviewSerializer,DirectorValidateSerializer,MovieValidateSerializer,ReviewValidateSerializer




STARS = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
)


# class UserConfirmation(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     confirmation_code = models.CharField(max_length=6, unique=True)
#     is_confirmed = models.BooleanField(default=False)
    
#     def save(self, *args, **kwargs):
#         if not self.confirmation_code:
#             self.confirmation_code = str(random.randint(100000, 999999))  
#         super().save(*args, **kwargs)



# @api_view(['GET', 'POST'])
# def director_list_api_view(request):
#  def director_list_create_api_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(serializer.data)
#         data = DirectorSerializer(directors, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = DirectorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director = Director.objects.create(name=serializer.validated_data['name'])
#         return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response({'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DirectorSerializer(director)
#         return Response(serializer.data)
#         data = DirectorSerializer(director).data
#         return Response(data=data)

#     elif request.method == 'PUT':
#         serializer = DirectorSerializer(director, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director.name = serializer.validated_data['name']
#         director.save()
#         return Response(data=DirectorSerializer(director).data)

#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movie_list_api_view(request):
#  def movie_list_create_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#         data = MovieSerializer(movies, many=True).data
#         return Response(data=data)

#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie = Movie.objects.create(
#             title=serializer.validated_data['title'],
#             description=serializer.validated_data['description'],
#             duration=serializer.validated_data['duration'],
#             director_id=serializer.validated_data['director_id']
#         )
#         return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#         data = MovieSerializer(movie).data
#         return Response(data=data)

#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = serializer.validated_data['title']
#         movie.description = serializer.validated_data['description']
#         movie.duration = serializer.validated_data['duration']
#         movie.director_id = serializer.validated_data['director_id']
#         movie.save()
#         return Response(data=MovieSerializer(movie).data)

#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#  def review_list_create_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#         data = ReviewSerializer(reviews, many=True).data
#         return Response(data=data)

#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review = Review.objects.create(
#             text=serializer.validated_data['text'],
#             movie_id=serializer.validated_data['movie_id'],
#             stars=serializer.validated_data['stars']
#         )
#         return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#         data = ReviewSerializer(review).data
#         return Response(data=data)

#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = serializer.validated_data['text']
#         review.movie_id = serializer.validated_data['movie_id']
#         review.stars = serializer.validated_data['stars']
#         review.save()
#         return Response(data=ReviewSerializer(review).data)

#     elif request.method == 'DELETE':
#         review.delete()




from rest_framework import serializers
from django.contrib.auth.models import User

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






        
 