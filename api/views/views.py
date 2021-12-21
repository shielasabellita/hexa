from django.shortcuts import render
from django.http import HttpResponse
from os import stat
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.utils.helpers import get_coa_csv_path
import pandas as pd



class TestView(APIView):
    def get(self, request, format=None):
        print(get_coa_csv_path())
        return Response("test rest api get", status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(request.data, status.HTTP_200_OK)


class TestViewCSV(APIView):
    def get(self, request, format=None):
        coa = pd.read_csv(get_coa_csv_path()).to_dict('records')

        return Response(coa, status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(request.data, status.HTTP_200_OK)



def welcome(request):
    return render(request, 'hello.html')
