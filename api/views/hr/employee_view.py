from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from api.utils.naming import set_naming_series

# models
from api.models import Employee

# serializers
from api.serializers.hr.employee_serializer import EmployeeSerializer

# other plugins
import pandas as pd
import json

# helpers
from api.utils.helpers import move_to_deleted_document



class EmployeeView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


    def get(self, request):
        try:
            id = request.GET.get('id', None)
            inst = Employee.objects.all().order_by("-updated_at")
            serializer = EmployeeSerializer(inst, many=True)

            if id != None:
                inst = get_object_or_404(Employee, id=id)
                serializer = EmployeeSerializer(inst)
            
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        data = request.data 

        data.update({
            "id": set_naming_series("EMP")
        })

        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        id = request.data['id']

        if id:
            inst = get_object_or_404(Employee.objects.all(), id=id)
            serializer = EmployeeSerializer(inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        ids = request.data['ids']
        
        for id in ids: 
            try:
                inst = get_object_or_404(Employee.objects.all(), id=id)
                move_to_deleted_document("Employee", id, json.dumps(model_to_dict(inst)), request.user)
                inst.delete()
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)