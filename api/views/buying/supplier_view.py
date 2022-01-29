from os import stat
from pkgutil import get_data
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from api import serializers
from api.models.accounting.accounting_group_model import WithHoldingTaxGroup

from api.models import CostCenter, PriceList, DiscountGroup, Supplier, SupplierGroup
from api.serializers.buying.supplier_serializer import SupplierSerializer
from api.views.stock.item_view import get_stock_doc


class SupplierView(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    
    model = Supplier
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        inst = self.model.objects.all()
        data = self.serializer_class(inst, many=True).data
        
        id = request.GET.get('id', None)
        if id:
            try:
                supplier = self.model.objects.get(id=id)
                data = self.serializer_class(supplier)
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response("Supplier not found", status=status.HTTP_404_NOT_FOUND)

        return Response(data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        post_data = request.data 
        try:
            supplier_data = self.set_data(post_data)
            supplier_inst = Supplier.objects.create(**supplier_data)
            
            return Response(self.serializer_class(supplier_inst).data)
        except Exception as e:
            return Response(str(e))
    
    def set_data(self, post_data):
        data = {
            "id": "{}_{}".format(str(post_data.get("sup_code")).upper(), str(post_data.get("sup_name")).upper()),
            "sup_code": post_data.get("sup_code"),
            "sup_name": post_data.get("sup_name"),
            "sup_shortname": post_data.get("sup_shortname"),
            "check_payee_name": post_data.get("check_payee_name"),
            "is_trucker": post_data.get("is_trucker"),
            "tax_identification_no": post_data.get("tax_identification_no"),
            "term": post_data.get("term"),
            "email": post_data.get("email"),
            "phone": post_data.get("phone"),
            "street": post_data.get("street"),
            "brgy": post_data.get("brgy"),
            "city": post_data.get("city"),
            "province": post_data.get("province"),
            "postal_code": post_data.get("postal_code"),
            "supplier_group": get_buying_doc("supplier_group", post_data.get("supplier_group")),
            "cost_center": get_buying_doc("costcenter", post_data.get("cost_center")),
            "vat_group": get_stock_doc("vat_group", post_data.get("vat_group")),
            "default_pricelist": PriceList.objects.get(id="Buying")
        }

        if post_data.get("wht"):
            data.update({"wht": get_buying_doc("wht", post_data.get("wht"))})
        
        if post_data.get("discount_group1"):
            data.update({"discount_group1": get_buying_doc("discount_group", post_data.get("discount_group1"))})
        
        if post_data.get("discount_group2"):
            data.update({"discount_group2": get_buying_doc("discount_group", post_data.get("discount_group2"))})
        
        if post_data.get("discount_group3"):
            data.update({"discount_group3": get_buying_doc("discount_group", post_data.get("discount_group3"))})
        
        post_expense = post_data.get("default_expense_account")
        if post_expense:
            data.update({"default_expense_account": get_stock_doc("coa", post_expense)})

        post_payable = post_data.get("default_payable_account")
        if post_payable:
            validate_payable_account(post_payable.split(" - ")[0])
            data.update({"default_payable_account": get_stock_doc("coa", post_data.get("default_payable_account"))})

        return data


def insert_supplier(data):
    Supplier.objects.create(**data)



def get_buying_doc(table_name, id):
    table = {
        "discount_group": DiscountGroup,
        "supplier_group": SupplierGroup,
        "costcenter": CostCenter,
        "wht": WithHoldingTaxGroup
    }

    obj = table[table_name].objects.get(id=id)
    return obj


def validate_payable_account(account_code, company=None):
    if account_code not in ("2000", "5040"):
        raise "Payable account must be either Progress Billing or Work in Progress"
        