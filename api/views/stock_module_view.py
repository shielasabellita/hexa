from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import ItemCategory, ItemCatBrand, ItemCatDepartment, ItemCatForm, ItemCatManufacturer, ItemCatSection, ItemCatSize
# serializers 
from api.serializers import ItemCategorySerializer, ItemCatBrandSerializer, ItemCatDepartmentSerializer, ItemCatFormSerializer, ItemCatManufacturerSerializer, ItemCatSectionSerializer, ItemCatSizeSerializer

class ItemCategoryView(APIView):
    
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            itemcats = ItemCategory.objects.all()
            itemcatsserializer = ItemCategorySerializer(itemcats, many=True)

            if id != None:
                itemcats = ItemCategory.objects.get(id=id)
                itemcatsserializer = ItemCategorySerializer(itemcats)
            
            data = itemcatsserializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        item_cat_srlzr = ItemCategorySerializer(data=request.data)
        if item_cat_srlzr.is_valid():
            item_cat_srlzr.save()

            return Response(item_cat_srlzr.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_cat_srlzr.errors, status=status.HTTP_400_BAD_REQUEST)