from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

# models
from api.models.stock.item_category_model import ItemCategory, ItemCatBrand, ItemCatDepartment, ItemCatForm, ItemCatManufacturer, ItemCatSection, ItemCatSize, UOM

# serializers 
from api.serializers.stock.category_management_serializer import *
from api.utils.helpers import move_to_deleted_document

import json

models_and_serializers = {
    "category": [ItemCategory, ItemCategorySerializer],
    "brand": [ItemCatBrand, ItemCatBrandSerializer],
    "department": [ItemCatDepartment, ItemCatDepartmentSerializer],
    "form": [ItemCatForm, ItemCatFormSerializer],
    "manufacturer": [ItemCatManufacturer, ItemCatManufacturerSerializer],
    "section": [ItemCatSection, ItemCatSectionSerializer],
    "size": [ItemCatSize, ItemCatSizeSerializer],
    "uom": [UOM, UOMSerializer]
}

class CategoryManagement(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def get(self, request, category):
        try:
            id = request.GET.get('id', None)
            inst = models_and_serializers[category][0].objects.all().order_by("-updated_at")
            serializer = models_and_serializers[category][1](inst, many=True)

            if id != None:
                inst = get_object_or_404(models_and_serializers[category][0], id=id)
                serializer = models_and_serializers[category][1](inst)
            
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, category):

        data = request.data
        if category == "uom":
            data.update({
                'id': data['uom']
            })

        serializer = models_and_serializers[category][1](data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, category):
        id = request.data['id']

        if id:
            inst = get_object_or_404(models_and_serializers[category][0].objects.all(), id=id)
            serializer = models_and_serializers[category][1](inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, category):
        ids = request.data['ids']
        
        for id in ids: 
            try:
                inst = get_object_or_404(models_and_serializers[category][0].objects.all(), id=id)
                move_to_deleted_document(category, id, model_to_dict(inst), request.user)
                inst.delete()
            except Exception as e:
                return Response("Error on ID {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)

