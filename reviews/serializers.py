from .models import Reviews
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'author', 'title', 'pub_date', 'body', 'imdb_ref', 'image', 'criticR']


