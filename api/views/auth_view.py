import django
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from api.serializers.auth_serializer import UserSerializer
from rest_framework.authtoken.models import Token


class LoginView(APIView):
    
    def post(self, request):
        data = request.data
        user = authenticate(username=data['usr'], password=data['pwd'])
        if user:
            user_serializer = UserSerializer(user)
            user_data = user_serializer.data
            user_data.pop('password')

            token = Token.objects.create(user=user)
            user_data.update({"token": token.key})

            return Response(user_data)
        else:
            return Response('Invalid credentials', status.HTTP_401_UNAUTHORIZED)

