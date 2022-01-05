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
from api.serializers.stock_module_serializer import *



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



class ItemCatBrandView(APIView):
    
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            itemcats = ItemCatBrand.objects.all()
            itemcatsserializer = ItemCatBrandSerializer(itemcats, many=True)

            if id != None:
                itemcats = ItemCatBrand.objects.get(id=id)
                itemcatsserializer = ItemCatBrandSerializer(itemcats)
            
            data = itemcatsserializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        item_cat_srlzr = ItemCatBrandSerializer(data=request.data)
        if item_cat_srlzr.is_valid():
            item_cat_srlzr.save()

            return Response(item_cat_srlzr.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_cat_srlzr.errors, status=status.HTTP_400_BAD_REQUEST)



class ItemCatDepartmentView(APIView):
    
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            itemcats = ItemCatDepartment.objects.all()
            itemcatsserializer = ItemCatDepartmentSerializer(itemcats, many=True)

            if id != None:
                itemcats = ItemCatDepartment.objects.get(id=id)
                itemcatsserializer = ItemCatDepartmentSerializer(itemcats)
            
            data = itemcatsserializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        item_cat_srlzr = ItemCatDepartmentSerializer(data=request.data)
        if item_cat_srlzr.is_valid():
            item_cat_srlzr.save()

            return Response(item_cat_srlzr.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_cat_srlzr.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemCatFormView(APIView):
    
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            itemcats = ItemCatForm.objects.all()
            itemcatsserializer = ItemCatFormSerializer(itemcats, many=True)

            if id != None:
                itemcats = ItemCatForm.objects.get(id=id)
                itemcatsserializer = ItemCatFormSerializer(itemcats)
            
            data = itemcatsserializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        item_cat_srlzr = ItemCatFormSerializer(data=request.data)
        if item_cat_srlzr.is_valid():
            item_cat_srlzr.save()

            return Response(item_cat_srlzr.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_cat_srlzr.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemCatManufacturerView(APIView):
    
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            itemcats = ItemCatManufacturer.objects.all()
            itemcatsserializer = ItemCatManufacturerSerializer(itemcats, many=True)

            if id != None:
                itemcats = ItemCatManufacturer.objects.get(id=id)
                itemcatsserializer = ItemCatManufacturerSerializer(itemcats)
            
            data = itemcatsserializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        item_cat_srlzr = ItemCatManufacturerSerializer(data=request.data)
        if item_cat_srlzr.is_valid():
            item_cat_srlzr.save()

            return Response(item_cat_srlzr.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_cat_srlzr.errors, status=status.HTTP_400_BAD_REQUEST)



class ItemCatSectionView(APIView):
    
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            itemcats = ItemCatSection.objects.all()
            itemcatsserializer = ItemCatSectionSerializer(itemcats, many=True)

            if id != None:
                itemcats = ItemCatSection.objects.get(id=id)
                itemcatsserializer = ItemCatSectionSerializer(itemcats)
            
            data = itemcatsserializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        item_cat_srlzr = ItemCatSectionSerializer(data=request.data)
        if item_cat_srlzr.is_valid():
            item_cat_srlzr.save()

            return Response(item_cat_srlzr.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_cat_srlzr.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemCatSizeView(APIView):
    
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            itemcats = ItemCatSize.objects.all()
            itemcatsserializer = ItemCatSizeSerializer(itemcats, many=True)

            if id != None:
                itemcats = ItemCatSize.objects.get(id=id)
                itemcatsserializer = ItemCatSizeSerializer(itemcats)
            
            data = itemcatsserializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        item_cat_srlzr = ItemCatSizeSerializer(data=request.data)
        if item_cat_srlzr.is_valid():
            item_cat_srlzr.save()

            return Response(item_cat_srlzr.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_cat_srlzr.errors, status=status.HTTP_400_BAD_REQUEST)