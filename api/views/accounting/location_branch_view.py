from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import Company, Branch, Location, CostCenter
from api.models.system_model import Series

# serializers
from api.serializers.accounting import LocationSerializer, BranchSerializer, CostCenterSerializer

# other plugins
import pandas as pd
import json

# helpers
from api.utils.helpers import move_to_deleted_document

from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from api.utils.naming import set_naming_series

models_and_serializers = {
    "branch": [Branch, BranchSerializer],
    "location": [Location, LocationSerializer],
    "costcenter": [CostCenter, CostCenterSerializer]
}

class LocationBranchView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


    def get(self, request, location):
        try:
            id = request.GET.get('id', None)
            inst = models_and_serializers[location][0].objects.all().order_by("-updated_at")
            serializer = models_and_serializers[location][1](inst, many=True)

            if id != None:
                inst = get_object_or_404(models_and_serializers[location][0], id=id)
                serializer = models_and_serializers[location][1](inst)
            
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, location):
        data = request.data 

        if location == "costcenter":
            data.update({
                "id": data['cost_center_name']
            })
        else:
            prefix = "BRC" if location == "branch" else "LOC"
            data.update({
                "id": set_naming_series(prefix)
            })

        serializer = models_and_serializers[location][1](data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, location):
        id = request.data['id']

        if id:
            inst = get_object_or_404(models_and_serializers[location][0].objects.all(), id=id)
            serializer = models_and_serializers[location][1](inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, location):
        ids = request.data['ids']
        
        for id in ids: 
            try:
                inst = get_object_or_404(models_and_serializers[location][0].objects.all(), id=id)
                move_to_deleted_document(location, id, json.dumps(model_to_dict(inst)), request.user)
                inst.delete()
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)