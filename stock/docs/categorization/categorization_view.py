from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document

from .categorization_model import *
from .categorization_serializer import *

import json
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from setup.docs.utils.helpers import move_to_deleted_document
from setup.docs.utils.naming import set_naming_series, generate_id

models_and_serializers = {
    "category": [ItemCategory, ItemCategorySerializer],
    "brand": [ItemCatBrand, ItemCatBrandSerializer],
    "department": [ItemCatDepartment, ItemCatDepartmentSerializer],
    "form": [ItemCatForm, ItemCatFormSerializer],
    "manufacturer": [ItemCatManufacturer, ItemCatManufacturerSerializer],
    "section": [ItemCatSection, ItemCatSectionSerializer],
    "size": [ItemCatSize, ItemCatSizeSerializer],
}


class CategorizationView(Document):

    def get(self, request, category):
        try:
            id = request.GET.get('id', None)
            filters = request.GET.get('filters', None)


            inst = models_and_serializers[category][0].objects.all().order_by("-updated_at")
            serializer = models_and_serializers[category][1](inst, many=True)
            
            if id != None:
                inst = get_object_or_404(models_and_serializers[category][0], id=id)
                serializer = models_and_serializers[category][1](inst)

            elif filters != None: 
                json_filters = json.loads(filters)
                inst = models_and_serializers[category][0].objects.filter(**json_filters)
                serializer = models_and_serializers[category][1](inst, many=True)
            
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, category):

        data = request.data
        code = set_naming_series(data['code'])
        
        data.update({
            "id": generate_id(),
            "code": code,
            "created_by": str(request.user),
            "updated_by": str(request.user),
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
            updated_data = request.data 
            updated_data.update({
                "updated_by": str(request.user)
            })
            serializer = models_and_serializers[category][1](inst, data=updated_data)
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


