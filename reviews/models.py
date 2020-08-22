from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Reviews(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True, auto_now=False)
    body = models.TextField()
    imdb_ref = models.CharField(max_length=20)
    image = models.ImageField(upload_to='film_image', null=True, blank=True, default="film_image/film_club.png")
    criticR = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.title
