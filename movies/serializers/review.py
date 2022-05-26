from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Review
from .comment import CommentSerializer

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('pk', 'username')

class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
            model = Movie
            fields = ('pk', 'title')


# movie review Read
class ReviewTitleSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    movie = MovieTitleSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'title', 'review_score', 'user', 'like_users', 'comments', 'movie', 'created_at',)


class ReviewSerializer(serializers.ModelSerializer):

    movie = MovieTitleSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'movie', 'user', 'title', 'content', 'review_score', 'created_at', 'updated_at', 'like_users', 'comments')
