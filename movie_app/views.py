from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Review, Director, UserConfirmation
from .serializers import MovieSerializer, ReviewSerializer, DirectorSerializer, MovieValidirySerializer, ReviewValiditySerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.models import User


class DirectorListAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer



class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


    def update_movie(self, movie, validated_data):
        movie.title = validated_data['title']
        movie.description = validated_data['description']
        movie.duration = validated_data['duration']
        movie.director = validated_data['director']
        movie.save()

    def perform_update(self, serializer):
        movie = self.get_object()
        self.update_movie(movie, serializer.validated_data)
        return movie


class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        validator = ReviewValiditySerializer(data=request.data)
        if validator.is_valid():
            review = Review.objects.create(**validator.validated_data)
            review.save()
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def update_review(self, review, validated_data):
        review.text = validated_data['text']
        review.movie = validated_data['movie']
        review.stars = validated_data['stars']
        review.save()

    def perform_update(self, serializer):
        review = self.get_object()
        self.update_review(review, serializer.validated_data)
        return review

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'message': 'User authenticated'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserConfirmAPIView(APIView):
    def post(self, request):
        confirmation_code = request.data.get('confirmation_code')
        try:
            user_confirmation = UserConfirmation.objects.get(confirmation_code=confirmation_code)
            if user_confirmation.is_confirmed:
                return Response({'message': 'User already confirmed'}, status=status.HTTP_400_BAD_REQUEST)
            user_confirmation.user.is_active = True
            user_confirmation.user.save()
            user_confirmation.is_confirmed = True
            user_confirmation.save()
            return Response({'message': 'User confirmed successfully'}, status=status.HTTP_200_OK)
        except UserConfirmation.DoesNotExist:
            return Response({'message': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)
