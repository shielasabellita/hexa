from os import stat
from pkgutil import get_data
from django.db.models.base import Model
from numpy import delete
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from api import serializers
from api.models.accounting.accounting_group_model import VatGroup
from api.models.defaults_model import PriceList
from api.models.setup_model import ChartOfAccounts

# models
from api.models.stock import Item, FixedAssetGroup, ItemGroup, ItemPrice, UOMConversionDetail, UOM
from api.models.buying import Supplier, SupplierItems

# serializers 
from api.serializers.stock import ItemSerializer
from api.serializers.stock.category_management_serializer import ItemPriceSerializer, SupplierItemsSerializer
from api.utils.helpers import move_to_deleted_document, get_company, get_doc
from api.utils.naming import set_naming_series

import json

class ItemView(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    
    model = Item
    serializer_class = ItemSerializer
    
    
    def get(self, request, *args, **kwargs): 
        inst = self.model.objects.all()
        data = self.serializer_class(inst, many=True).data
        
        id = request.GET.get('id', None)

        if id:
            try:
                item = self.model.objects.get(id=id)
                data = self.get_data(item)
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response("Item not found", status=status.HTTP_404_NOT_FOUND)

        return Response(data, status=status.HTTP_200_OK)



    def post(self, request):
        data = self.set_data(request.data)
        try:
            item = insert_item(data)
            data = self.get_data(item)
            return Response(data)
        except Exception as e:
            return Response(str(e))



    def put(self, request, *args, **kwargs):
        id = request.data['item_code']

        request.data.update({"id": id})

        if id:
            inst = get_object_or_404(self.model.objects.all(), id=id)
            serializer = self.serializer_class(inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = self.get_data(inst)
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, *args, **kwargs):
        ids = request.data['ids']
        
        for id in ids: 
            try:
                inst = get_object_or_404(self.model.objects.all(), id=id)
                move_to_deleted_document("Item", id, json.dumps(model_to_dict(inst)), request.user)
                
                inst.delete() 
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)
    
    def get_data(self, item):
        item_data = self.serializer_class(item).data
        item_data.update({
            "conversion_detail": [],
            "item_prices": [],
            "supplier_items": [],

        })

        for i in UOMConversionDetail.objects.filter(item=item.id):
            item_data['conversion_detail'].append({
                "id": i.id,
                "uom": i.uom.id,
                "conversion_factor": i.conversion_factor
            })

        for i in ItemPrice.objects.filter(item=item.id):
            item_data['item_prices'].append({
                "price_list": i.price_list.id,
                "id": i.id,
                "price": i.price,
                "uom": i.base_uom.id
            })

        for i in SupplierItems.objects.filter(item=item.id):
            item_data['supplier_items'].append(SupplierItemsSerializer(i).data)

        return item_data


    def set_data(self, post_data):
        data = {
            "sku_code": post_data.get('sku_code'),
            "item_barcode": post_data.get('item_barcode'),
            "item_name": post_data.get('item_name'),
            "item_shortname": post_data.get('item_shortname'),
            "base_uom": post_data.get('base_uom'),
            "expiry": post_data.get('expiry'),
            "serial_no": post_data.get('serial_no'),
            "batch_no": post_data.get('batch_no'),
            
            "vat_group": post_data.get('vat_group'),
            "default_income_account": post_data.get('default_income_account'),
            "default_cos_account": post_data.get('default_cos_account'), 

            "is_fixed_asset": post_data.get('is_fixed_asset'),
            "maintain_stock": post_data.get('maintain_stock'),
            "item_group": "Product" if post_data.get('maintain_stock') == 1 else "Asset",
            
            "is_purchase_item": post_data.get('is_purchase_item'),
            "purchase_uom": post_data.get('purchase_uom'),
            "is_sales_item": post_data.get('is_sales_item'),
            "sales_uom": post_data.get('sales_uom'),
            
            "conversion_detail": [],
            "supplier_items": [],

            "buying_price_uom": post_data.get('buying_price_uom'),  
            "selling_price_uom": post_data.get('selling_price_uom'),  
            "transfer_price_uom": post_data.get('transfer_price_uom'),  

        }

        for i in post_data.get('conversion_detail'):
            data['conversion_detail'].append(i)

        for i in post_data.get('supplier_items'):
            data['supplier_items'].append(i)

        if post_data.get('item_group'):
            data.update({
                "item_group": post_data.get('item_group')
            })
        
        if post_data.get("is_fixed_asset"):
            if post_data.get("fixed_asset_group"):
                data.update({
                    "fixed_asset_group": post_data.get("fixed_asset_group") 
                })
            else:
                raise "Please add Fixed Asset Group"
        else:
            data.update({"fixed_asset_group": ""})

        company = get_company(post_data['company'])
        if not data['default_income_account']:
            if data['item_group'] in ["Product"]:
                data.update({
                        "default_income_account": "4010 - Sales"
                    })
            elif data['item_group'] in ['Material']:
                data.update({
                    "default_income_account": "4000 - Revenue"
                })

        if not data['default_cos_account']:
            if data['item_group'] in ["Product"]:
                data.update({
                        "default_cos_account": "5050 - Cost of Sales"
                    })
            elif data['item_group'] in ['Material']:
                data.update({
                    "default_cos_account": "5000 - Labor - COS"
                })


        return data





class ItemDetailsView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def post(self, request, item_detail):
        request_data = request.data 

        try:
            item = get_stock_doc("item", request_data.get("item_code"))
            request_data.update({
                "item": item
            })
            request_data.pop("item_code")
            
            if item_detail == "item_price":
                insert_item_price(request_data)
            elif item_detail == "supplier_items":
                insert_supplier_items(request_data)

            itemview = ItemView()
            data = itemview.get_data(item)
            return Response(data)
        except Exception as e:
            return Response(str(e))


    def put(self, request, item_detail):
        request_data = request.data

        if request_data.get("id"):
            item = get_stock_doc("item", request_data.get("item_code"))

            request_data.update({
                "item": request_data.get("item_code")
            })
            request_data.pop("item_code")
            
            if item_detail == "item_price":
                inst = get_object_or_404(ItemPrice.objects.all(), id=request_data.get("id"))
                serializer = ItemPriceSerializer(inst, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif item_detail == "supplier_items":
                try:
                    inst = get_object_or_404(SupplierItems.objects.all(), id=request_data.get("id"))
                    inst.supplier = get_stock_doc("supplier", request_data['supplier'])
                    inst.item = item
                    inst.save()
                    return Response(SupplierItemsSerializer(inst).data)
                except Exception as e:
                    return Response(str(e))
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, item_detail):
        ids = request.data['ids']
        model_serializer = {
            "item_price": [ItemPrice, ItemPriceSerializer],
            "supplier_items": [SupplierItems, SupplierItemsSerializer]
        }
        for id in ids: 
            try:
                inst = get_object_or_404(model_serializer[item_detail][0], id=id)
                move_to_deleted_document(item_detail, id, json.dumps(model_to_dict(inst)), request.user)
                
                inst.delete() 
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)



# insert item
def insert_item(data):
    item_id = set_naming_series("ITM")
    item_data = {
        "id": item_id,
        "item_code": item_id,
        "sku_code": data['sku_code'],
        "item_barcode": data['item_barcode'],
        "item_name": data['item_name'],
        "item_shortname": data['item_shortname'],
        "is_fixed_asset": data['is_fixed_asset'],
        "maintain_stock": data['maintain_stock'],
        "serial_no": data['serial_no'],
        "batch_no": data['batch_no'],
        "expiry": data['expiry'],

        "is_purchase_item": data['is_purchase_item'],
        "purchase_uom": get_stock_doc("uom", data['purchase_uom']), # FK

        "is_sales_item": data['is_sales_item'],
        "sales_uom": get_stock_doc("uom", data['sales_uom']), #FK

        "base_uom": get_stock_doc("uom", data['base_uom']), #FK 
        "item_group": get_stock_doc("item_group", data['item_group']), #FK
        
        "vat_group": get_stock_doc("vat_group", data['vat_group']), #FK
        "default_income_account": get_stock_doc("coa", data['default_income_account']), #FK
        "default_cos_account": get_stock_doc("coa", data['default_cos_account']), #FK
    }

    if data['fixed_asset_group']:
        item_data.update({
            "fixed_asset_group": get_stock_doc("fixed_asset", data['fixed_asset_group']), #FK
        })
    item = Item.objects.create(**item_data)

    # supplier items
    if data['supplier_items']:
        for sup in data['supplier_items']:
            sup.update({
                "item": item
            })
            insert_supplier_items(data = sup)

    # conversion factor
    if data['conversion_detail']:
        for uom in data['conversion_detail']:
            uom.update({
                "item": item
            })
            insert_conversion_detail(data = uom)
    else: 
        insert_conversion_detail(data={
            "conversion_factor": 1,
            "uom": get_stock_doc("uom", data['base_uom']),
            "item": item,
        })

    # item price
    item_prices_data = [
        {
            "price_list": "Buying",
            "price": data['buying_price_uom'],
            "item": item,
            "base_uom": data['base_uom'] if not data['purchase_uom'] else data['purchase_uom']
        },
        {
            "price_list": "Selling",
            "price": data['selling_price_uom'],
            "item": item,
            "base_uom": data['base_uom'] if not data['sales_uom'] else data['sales_uom']
        },
        {
            "price_list": "Transfer",
            "price": data['transfer_price_uom'],
            "item": item,
            "base_uom": data['base_uom']
        },
    ]

    for price in item_prices_data:
        insert_item_price(price)

    return item

# insert item price
def insert_item_price(data):
    item_price_id = "{}-{}-{}".format(data['item'].id, data['price_list'], data['base_uom'])
    data.update({
            "id": item_price_id,
            "price_list": get_stock_doc("price_list", data['price_list']),
            "base_uom": get_stock_doc("uom", data['base_uom']),
            "price": data['price'],
            "item": data['item']  ## item must be instance
        })
    ItemPrice.objects.create(**data)
    

def insert_conversion_detail(data):
    UOMConversionDetail.objects.create(**data)


def insert_supplier_items(data):
    supplier_items_data = {
        "supplier": get_stock_doc("supplier", data['supplier']),
        "item": data['item'], ## item must be an instance
    }

    SupplierItems.objects.create(**supplier_items_data)


def get_stock_doc(table_name, id):
    table = {
        "uom": UOM, 
        "item_group": ItemGroup,
        "vat_group": VatGroup,
        "coa": ChartOfAccounts,
        "fixed_asset": FixedAssetGroup,
        "price_list": PriceList,
        "supplier": Supplier,
        "item": Item
    }
    
    obj = table[table_name].objects.get(id=id)
    return obj