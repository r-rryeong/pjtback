from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Comment


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')


class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'created_at', 'review')
        read_only_fields = ('review',)