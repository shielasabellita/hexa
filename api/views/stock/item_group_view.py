from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import stock


# models
from api.models.stock import FixedAssetGroup, ItemGroup
from api.models.defaults_model import PriceList

# serializers 
from api.serializers.stock import ItemSerializerGroup, FixedAssetGroupSerializer, PriceListSerializer
from api.utils.helpers import move_to_deleted_document
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import json


models_and_serializers = {
    "item_group": [ItemGroup, ItemSerializerGroup],
    "fixed_asset_group": [FixedAssetGroup, FixedAssetGroupSerializer],
    "price_list": [PriceList, PriceListSerializer]
}

class StockGroup(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


    def get(self, request, stock_group):
        inst = models_and_serializers[stock_group][0].objects.all().order_by("-updated_at")
        data = models_and_serializers[stock_group][1](inst, many=True).data

        id = request.GET.get('id', None)

        if id:
            try:
                inst = models_and_serializers[stock_group][0](id=id)
                data = models_and_serializers[stock_group][1](inst).data
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_404_NOT_FOUND)

        return Response(data, status=status.HTTP_200_OK)



    def post(self, request, stock_group):
        data = request.data
        
        data.update({
            "id": data[stock_group]
        })

        serializer = models_and_serializers[stock_group][1](data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, stock_group):
        id = request.data['id']

        if id:
            inst = get_object_or_404(models_and_serializers[stock_group][0].objects.all(), id=id)
            serializer = models_and_serializers[stock_group][1](inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, stock_group):
        ids = request.data['ids']
        
        for id in ids: 
            try:
                inst = get_object_or_404(models_and_serializers[stock_group][0].objects.all(), id=id)
                move_to_deleted_document(stock_group, id, model_to_dict(inst), request.user)
                inst.delete()
            except Exception as e:
                return Response("Error on {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)

