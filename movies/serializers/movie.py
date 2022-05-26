from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Genre, Comingsoon, Boxoffice
from .review import ReviewTitleSerializer

# serializer 기능
# CUD : validation
# R : data serializing

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('pk', 'username')

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    is_watched = UserSerializer(many=True, read_only=True)
    reviews = ReviewTitleSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'genres', 'release_date', 'vote_average', 'popularity', 'overview', 'poster_path', 'video', 'like_users', 'is_watched', 'reviews',)


class MovieDetailSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    is_watched = UserSerializer(many=True, read_only=True)
    reviews = ReviewTitleSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'genres', 'release_date', 'vote_average', 'overview', 'poster_path', 'backdrop_path', 'video', 'like_users', 'is_watched', 'reviews')


class ComingsoonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comingsoon
        fields = '__all__'


class BoxofficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boxoffice
        fields = '__all__'