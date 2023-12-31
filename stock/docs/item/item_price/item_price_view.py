from warnings import filters
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from setup.core.doc import Document

# model
from .item_price_model import ItemPrice

# serializer
from .item_price_serializer import ItemPriceSerializer

# other packages
import json


class ItemPriceView(Document):
    model = ItemPrice
    serializer = ItemPriceSerializer

    def __init__(self, *args, **kwargs):
        args = (ItemPrice, ItemPriceSerializer)
        super().__init__(*args,**kwargs)

    # API - GET
    def get(self, request, *args, **kwargs):
        try:
            if request.GET.get('filters', None):
                data = self.get_list(filters=json.loads(request.GET.get('filters', None)))
            else:
                id = request.GET.get('id', None)
                data = self.get_list(id)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - POST
    def post(self, request, *args, **kwargs):
        data = request.data 
        try:
            if not self.validate_duplicate_price(data.get('item'), data.get('supplier'), data.get("base_uom"), data.get('price_list')):

                if not data.get("code"):
                    code = self.model._meta.get_field("code").default
                    data.update({
                        "code": code
                    })

                data = self.create(data, user=str(request.user))
                return Response(data)
            else:
                raise Exception("Cannot add multiple prices with the same uom")
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - PUT
    def put(self, request, *args, **kwargs):
        data = request.data 
        try:
            if not self.validate_duplicate_price(data.get('item'), data.get('supplier'), data.get("base_uom"), data.get('price_list')):
                data = self.update(id=data.get('id'), data=data, user=str(request.user))
                return Response(data)
            else:
                raise Exception("Cannot add multiple prices with the same uom")
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



    def validate_duplicate_price(self, item, supplier, uom, price_list):
        filters= {
            "item": item, 
            "supplier": supplier,
            "base_uom": uom, 
            "price_list": price_list,
        }
        if len(self.get_list(filters=filters)) > 0:
            return True
        else:
            return False