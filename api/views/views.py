from django.shortcuts import render
from django.http import HttpResponse
from os import stat
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, format=None):
        return Response("test rest api get", status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(request.data, status.HTTP_200_OK)




def welcome(request):
    return render(request, 'hello.html')
