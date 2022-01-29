from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# models
from api.models import VatGroup, DiscountGroup, SupplierGroup, WithHoldingTaxGroup

# serializers
from api.serializers.accounting.accounting_group_serializer import *

from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from api.utils.helpers import move_to_deleted_document
import json


models_and_serializers = {
    "vat_group": [VatGroup, VatGroupSerializer],
    "discount_group": [DiscountGroup, DiscountGroupSerializer],
    "supplier_group": [SupplierGroup, SupplierGroupSerializer],
    "wht_group": [WithHoldingTaxGroup, WithHoldingTaxGroupSerializer],
}


class AccountingGroup(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]


    def get(self, request, group, *args, **kwargs):
        try:
            id = request.GET.get('id', None)
            inst = models_and_serializers[group][0].objects.all()
            serializer = models_and_serializers[group][1](inst, many=True)

            if id != None:
                inst = get_object_or_404(models_and_serializers[group][0], id=id)
                serializer = models_and_serializers[group][1](inst)
            
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, group, *args, **kwargs):
        try:
            data = request.data
            data.update({
                "id": self.generate_id(group,data)
            })

            if group == "discount_group":
                data.update({
                    "total_discount": sum([data['discount1'], data['discount2'], data['discount3']])
                })


            serializer = models_and_serializers[group][1](data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,  status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, group):
        id = request.data['id']

        if id:
            inst = get_object_or_404(models_and_serializers[group][0].objects.all(), id=id)
            serializer = models_and_serializers[group][1](inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, group): 
        ids = request.data['ids']
        
        for id in ids: 
            try:
                inst = get_object_or_404(models_and_serializers[group][0].objects.all(), id=id)
                move_to_deleted_document(group, id, json.dumps(model_to_dict(inst)), request.user)
                inst.delete()
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)


    def generate_id(self, group, data):
        if group == 'vat_group':
            return "{} - {}".format(data['vat_group_code'], data['vat_group_name'])
        elif group == "discount_group": 
            return data['discount_name']
        elif group == 'supplier_group':
            return data['id']
        elif group == 'wht_group':
            return "{} - {}".format(data['wht_code'],data['wht_name'])