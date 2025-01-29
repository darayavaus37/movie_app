
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Director, Movie, Review, UserConfirmation
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, UserSerializer, UserConfirmationSerializer


class DirectorListAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


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
        



