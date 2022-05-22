

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from setup.core.doc import Document

# model / serializer
from stock.docs.item_group.item_group_serializer import ItemGroupSerializer, ItemGroup
from stock.docs.uom.uom_serializer import UOMSerializer, UOM
from accounting.docs.chart_of_accounts.chart_of_accounts_serializer import ChartOfAccountsSerializer, ChartOfAccounts
from accounting.docs.vat_group.vat_group_serializer import VatGroupSerializer, VatGroup
from .item_serializer import ItemSerializer, Item

# other packages
import json


class ItemView(Document):
    fk_fields = ['purchase_uom', 'base_uom', 'sales_uom', 'item_group', 'fixed_asset_group',
                'vat_group', 'default_income_account', 'default_cos_account'
            ]
    fk_models_serializer = {
        'purchase_uom': [UOM, UOMSerializer], 
        'base_uom': [UOM, UOMSerializer], 
        'sales_uom': [UOM, UOMSerializer], 
        'item_group': [ItemGroup, ItemGroupSerializer], 
        'fixed_asset_group': [ItemGroup, ItemGroupSerializer],
        'vat_group': [VatGroup, VatGroupSerializer], 
        'default_income_account': [ChartOfAccounts, ChartOfAccountsSerializer], 
        'default_cos_account': [ChartOfAccounts, ChartOfAccountsSerializer]
    }

    def __init__(self, *args, **kwargs):
        args = (Item, ItemSerializer)
        super().__init__(*args,**kwargs)

    # API - GET
    def get(self, request, *args, **kwargs):
        try:
            if request.GET.get('filters', None):
                data = self.get_list(filters=json.loads(request.GET.get('filters', None)), fk_fields=self.fk_fields, models_serializer=self.fk_models_serializer)
            else:
                id = request.GET.get('id', None)
                data = self.get_list(id, fk_fields=self.fk_fields, models_serializer=self.fk_models_serializer)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - POST
    def post(self, request, *args, **kwargs):
        data = request.data 
        try:
            data = self.create(data, user=str(request.user))
            return Response(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - PUT
    def put(self, request, *args, **kwargs):
        data = request.data 
        try:
            data = self.update(id=data.get("id"), data=data, user=str(request.user))
            return Response(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - DELETE
    def delete(self, request, *args, **kwargs):
        ids = request.data['ids']
        for id in ids: 
            try:
                self.remove(id, request.user)
            except Exception as e:
                return Response("Error on ID {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)



       