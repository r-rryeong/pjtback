from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path')

class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
    
        movie = MovieSerializer(read_only=True)
        class Meta:
            model = Review
            fields = ('pk', 'movie', 'title', 'review_score', 'created_at',)

    like_movies = MovieSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    watch_movie = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_movies', 'reviews', 'watch_movie')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'is_superuser', 'is_staff',)
