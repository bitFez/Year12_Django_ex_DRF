from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    no_reviews = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='profiles', null=True, blank=True, default='profiles/profile.png')
    insta = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.author.username
