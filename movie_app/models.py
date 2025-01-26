from django.db import models
from django.contrib.auth.models import User
import random



class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()  
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


STARS = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
)

class Review(models.Model):
    text = models.TextField(null=True, blank=True) 
    movie = models.ForeignKey(Movie, 
                              on_delete=models.CASCADE,
                              related_name='reviews')  
    stars = models.IntegerField(choices=STARS)  

    stars = models.IntegerField()

    def __str__(self):
        return f'Отзыв фильма: {self.movie.title} - {self.stars} '
    


    def generate_confirmation_code(self):
        self.confirmation_code = str(random.randint(100000, 999999))
        self.save()
        return self.confirmation_code




class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=6)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Confirmation for {self.user.username}"




        
 