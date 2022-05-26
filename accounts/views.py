from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer, UserInfoSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    

@api_view(['GET'])
def user_info(request):
    user = request.user
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), pk=user.pk)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)