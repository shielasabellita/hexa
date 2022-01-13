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

class AccountingGroup(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]

    def get(self, request, group, *args, **kwargs):
        try:
            models_and_serializers = {
                "vat_group": [VatGroup, VatGroupSerializer],
                "discount_group": [DiscountGroup, DiscountGroupSerializer],
                "supplier_group": [SupplierGroup, SupplierGroupSerializer],
                "wht_group": [WithHoldingTaxGroup, WithHoldingTaxGroupSerializer],
            }
            if request.data:
                inst = models_and_serializers[group][0].objects.filter(id=request.data['id'])
                data = models_and_serializers[group][1](inst).data
            else:
                inst = models_and_serializers[group][0].objects.all()
                data = models_and_serializers[group][1](inst, many=True).data

            return Response(data,  status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def post(self, request, group, *args, **kwargs):
        try:
            models_and_serializers = {
                "vat_group": [VatGroup, VatGroupSerializer],
                "discount_group": [DiscountGroup, DiscountGroupSerializer],
                "supplier_group": [SupplierGroup, SupplierGroupSerializer],
                "wht_group": [WithHoldingTaxGroup, WithHoldingTaxGroupSerializer],
            }
            data = request.data
            data.update({
                "id": self.generate_id(group,data)
            })
            serializer = models_and_serializers[group][1](data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,  status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def generate_id(self, group, data):
        if group == 'vat_group':
            return "{} - {}".format(data['vat_group_code'], data['vat_group_name'])
        elif group == "discount_group": 
            return data['discount_name']
        elif group == 'supplier_group':
            return data['id']
        elif group == 'wht_group':
            return "{} - {}".format(data['wht_code'],data['wht_name'])