from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import ItemCategory, ItemCatBrand, ItemCatDepartment, ItemCatForm, ItemCatManufacturer, ItemCatSection, ItemCatSize
# serializers 
from api.serializers.stock.stock_module_serializer import *

models_and_serializers = {
    "category": [ItemCategory, ItemCategorySerializer],
    "brand": [ItemCatBrand, ItemCatBrandSerializer],
    "department": [ItemCatDepartment, ItemCatDepartmentSerializer],
    "form": [ItemCatForm, ItemCatFormSerializer],
    "manufacturer": [ItemCatManufacturer, ItemCatManufacturerSerializer],
    "section": [ItemCatSection, ItemCatSectionSerializer],
    "size": [ItemCatSize, ItemCatSizeSerializer],
}

class CategoryManagement(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def get(self, request, category):
        try:
            id = request.GET.get('id', None)
            inst = models_and_serializers[category][0].objects.all()
            serializer = models_and_serializers[category][1](inst, many=True)

            if id != None:
                inst = models_and_serializers[category][0].objects.get(id=id)
                serializer = models_and_serializers[category][1](inst)
            
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, category):
        serializer = models_and_serializers[category][1](data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

