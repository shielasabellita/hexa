from django.db.models.base import Model
from numpy import insert
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from setuptools import Require
from api import serializers
from api.models.accounting.accounting_group_model import WithHoldingTaxGroup

from api.models import CostCenter, PriceList, DiscountGroup, Supplier, SupplierGroup, SupplierDiscounts
from api.serializers.buying.supplier_serializer import SupplierDiscountsSerializer, SupplierSerializer
from api.views.stock.item_view import get_stock_doc
from api.utils.helpers import move_to_deleted_document, get_company, get_doc
from api.utils.naming import set_naming_series
import json


class SupplierView(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    
    model = Supplier
    serializer_class = SupplierSerializer

    def get(self, request):
        inst = self.model.objects.all().order_by("-updated_at")
        data = self.serializer_class(inst, many=True).data
        
        id = request.GET.get('id', None)
        if id:
            try:
                supplier = self.model.objects.get(id=id)
                data = self.get_data(supplier)
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e))

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            inst = insert_supplier(request.data)
            data = self.get_data(inst)
            return Response(data)
        except Exception as e:
            return Response(str(e))

    def put(self, request):
        request_data = request.data

        if request_data.get("id"):
            inst = Supplier.objects.get(id=request_data.get("id"))
            serializer = SupplierSerializer(inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(self.get_data(inst), status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response("Please enter a valid ID", status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request):
        ids = request.data['ids']
        for id in ids: 
            try:
                inst = Supplier.objects.get(id=id)
                move_to_deleted_document("Supplier", id, json.dumps(model_to_dict(inst)), request.user)
                inst.delete() 
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)


    def get_data(self, supplier):
        supplier_data = self.serializer_class(supplier).data
        supplier_discs_insts = SupplierDiscounts.objects.filter(supplier=supplier)
        supplier_discs_data = SupplierDiscountsSerializer(supplier_discs_insts, many=True).data
        supplier_data.update({
            "discount_groups": supplier_discs_data
        })

        return supplier_data


def insert_supplier(data):
    sup_id = set_naming_series("SUP")
    supplier_data = data
    discount_groups = data.get("discount_groups")
    supplier_data.pop("discount_groups")
    supplier_data.update({
        "id": sup_id
    })

    serializer = SupplierSerializer(data=supplier_data)
    if serializer.is_valid():
        serializer.save()
        supplier_inst = Supplier.objects.get(id=sup_id)

        if discount_groups:
            for disc in discount_groups:
                if not SupplierDiscounts.objects.filter(discount_group=disc, supplier=sup_id):
                    save_supplier_discount(disc, supplier_inst)
                else:
                    save_supplier_discount(disc, supplier_inst, method="update", id=disc)

        return supplier_inst


def save_supplier_discount(disc_group, supplier_inst, method="create", id=None):
    discount_group_inst = DiscountGroup.objects.get(id=disc_group)
    dt = {
        "supplier": supplier_inst,
        "discount_group": discount_group_inst
    }
    if method=="create":
        SupplierDiscounts.objects.create(**dt)
    else:
        disc_inst = SupplierDiscounts.objects.get(id=id)
        disc_inst.discount_group = discount_group_inst
        disc_inst.suplier = supplier_inst
        disc_inst.save()

    sup_discs = SupplierDiscounts.objects.filter(supplier=supplier_inst)
    return SupplierDiscountsSerializer(instance=sup_discs, many=True)



class SupplierDiscountView(APIView):
    model = SupplierDiscounts
    serializer_class = SupplierDiscountsSerializer
    
    def get(self, request):
        inst = self.model.objects.all()
        data = self.serializer_class(inst, many=True).data

        id = request.GET.get('id', None)
        if id:
            try:
                inst = self.model.objects.get(id=id)
                data = self.serializer_class(inst).data
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e))

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data
        try:
            supplier_discount = save_supplier_discount(
                disc_group = request_data.get("discount_group"),
                supplier_inst = Supplier.objects.get(id=request_data.get("supplier")),
                method = "create"
            )
            return Response(supplier_discount.data)
        except Exception as e:
            return Response(str(e))

    def put(self, request):
        request_data = request.data
        try:
            supplier_discount = save_supplier_discount(
                disc_group = request_data.get("discount_group"),
                supplier_inst = Supplier.objects.get(id=request_data.get("supplier")),
                method = "update",
                id = request_data.get("id")
            )
            return Response(supplier_discount.data)
        except Exception as e:
            return Response(str(e))

    def delete(self, request):
        ids = request.data['ids']
        for id in ids: 
            try:
                inst = SupplierDiscounts.objects.get(id=id)
                move_to_deleted_document("Supplier Discount", id, json.dumps(model_to_dict(inst)), request.user)
                inst.delete() 
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("Successfully deleted", status=status.HTTP_200_OK)
