from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),  
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()), 
    path('api/v1/movies/', views.MovieListAPIView.as_view()),  
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view()),  
    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),  
    path('api/v1/reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),  
    path('api/v1/users/register/', views.UserRegisterAPIView.as_view(), name='user_register'),
    path('api/v1/users/login/', views.UserLoginAPIView.as_view(), name='user_login'),
    path('api/v1/users/confirm/', views.UserConfirmAPIView.as_view(), name='user_confirm'),
]









