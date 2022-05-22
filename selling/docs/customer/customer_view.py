from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document

# serializer
from .customer_serializer import CustomerSerializer, Customer

from accounting.docs.chart_of_accounts.chart_of_accounts_serializer import ChartOfAccountsSerializer, ChartOfAccounts
from accounting.docs.cost_center.cost_center_serializer import CostCenterSerializer, CostCenter
from accounting.docs.price_list.price_list_serializer import PriceListSerializer, PriceList
from accounting.docs.vat_group.vat_group_serializer import VatGroupSerializer, VatGroup
from accounting.docs.withholding_tax_group.withholding_tax_serializer import WithHoldingTaxGroupSerializer, WithHoldingTaxGroup

import json

class CustomerView(Document):
    fk_fields = [
            "cost_center", "vat_group", "wht", 
            "default_pricelist", "default_receivable_account"
            ]

    fk_models_serializer = {
            "cost_center": [CostCenter, CostCenterSerializer],
            "vat_group": [VatGroup, VatGroupSerializer],
            "wht": [WithHoldingTaxGroup, WithHoldingTaxGroupSerializer],
            "default_pricelist": [PriceList, PriceListSerializer],
            "default_receivable_account": [ChartOfAccounts, ChartOfAccountsSerializer]
        }

    def __init__(self, *args, **kwargs):
        args = (Customer, CustomerSerializer)
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