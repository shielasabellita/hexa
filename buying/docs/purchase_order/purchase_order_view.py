import json
from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document
from stock.docs.item.item_model import Item
from stock.docs.uom.uom_model import UOM

from .purchase_order_serializer import PurchaseOrderSerializer, PurchaseOrder
from accounting.docs.pricing_rule.pricing_rule_apply_to.apply_to_item_supplier_model import ApplyTo
from accounting.docs.pricing_rule.pricing_rule_model import PricingRule
from buying.docs.purchase_order.po_items.po_items_serializer import POItemsSerializer
from buying.docs.purchase_order.po_items.po_items_view import POItemsView

from accounting.docs.price_list.price_list_serializer import PriceListSerializer, PriceList
from accounting.docs.cost_center.cost_center_serializer import CostCenterSerializer, CostCenter
from setup.docs.branch.branch_serializer import Branch, BranchSerializer
from setup.docs.location.location_serializer import LocationSerializer, Location
from stock.docs.item_group.item_group_serializer import ItemGroupSerializer, ItemGroup
from setup.docs.reason_codes.reason_codes_serializer import StatusAndRCodeSerializer, StatusAndRCode
from stock.docs.fixed_asset_group.fixed_asset_serializer import FixedAssetGroupSerializer, FixedAssetGroup
from buying.docs.supplier.supplier_serializer import Supplier, SupplierSerializer
from .po_items.po_items_model import POItems

from controller.utils import get_percent, flt
# utils
# from buying.docs.buying_controller import get_rate

class PurchaseOrderView(Document):
    fk_fields = [
            "reason_code", "item_group", "fixed_asset_group", 
            "supplier", "cost_center", "branch", "location", "price_list"
            ]

    fk_models_serializer = {
            "supplier": [Supplier, SupplierSerializer], 
            "reason_code": [StatusAndRCode, StatusAndRCodeSerializer], 
            "item_group": [ItemGroup, ItemGroupSerializer], 
            "fixed_asset_group": [FixedAssetGroup, FixedAssetGroupSerializer], 
            "supplier": [Supplier, SupplierSerializer], 
            "cost_center": [CostCenter, CostCenterSerializer], 
            "branch": [Branch, BranchSerializer], 
            "location": [Location, LocationSerializer], 
            "price_list": [PriceList, PriceListSerializer]
        }
    
    poitems_doc = POItemsView(POItems, POItemsSerializer)
    
    obj = {}
    net_amount = 0
    total_amount = 0
    items = []
    
    def __init__(self, *args, **kwargs):
        args = (PurchaseOrder, PurchaseOrderSerializer)
        super().__init__(*args,**kwargs)

    # API - GET
    def get(self, request, *args, **kwargs):
        try:
            if request.GET.get('filters', None):
                data = self.get_list(filters=json.loads(request.GET.get('filters', None)), fk_fields=self.fk_fields, models_serializer=self.fk_models_serializer)
                for d in data:
                    d.update(self.get_child_data(d['id']))
            else:
                id = request.GET.get('id', None)
                data = self.get_list(id, fk_fields=self.fk_fields, models_serializer=self.fk_models_serializer)
                if data:
                    if len(data) > 1:
                        for d in data:
                            d.update(self.get_child_data(d['id']))
                    else:
                        data.update(self.get_child_data(data['id']))

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get_child_data(self, parent):
        obj = {
            "items": self.poitems_doc.get_list(filters={"purchase_order": parent})
        }
        return obj


    # API - POST
    def post(self, request):
        data = request.data
        
        self.set_po_obj(data)
        if not data.get('items'):
            raise Exception("Items is required")
        else:
            self.items = self.set_poitems_obj(data.get('items'))

        serialized_po_data = self.create(self.obj, user=str(request.user))
        serialized_po_data.update({
            "items": []
        })
        if serialized_po_data:
            po_doc = PurchaseOrder.objects.get(id=serialized_po_data['id'])
            for itm in self.items:
                itm.update({
                    "purchase_order": po_doc.id,
                })
                
                po_item_data = self.poitems_doc.create(data=itm, user=str(request.user))
                serialized_po_data['items'].append(po_item_data)
                
        return Response(serialized_po_data)


    def set_po_obj(self, data):
        self.obj.update({
            "date": data['date'],
            "date_expected": data['date_expected'],
        })
        self.validate_item_group(data)
        self.location(data)
        self.supplier(data)
        self.price_list(data)

        if data.get("reason_code"):
            self.reason_code(data.get("reason_code"))
        

    def supplier(self, data):
        supplier = self.fk_models_serializer['supplier'][0].objects.get(id=data["supplier"])
        self.obj.update({
            "supplier": supplier.id
        })
        return supplier
    
    def reason_code(self, data_reason_code):
        reason_code = self.fk_models_serializer['reason_code'][0].objects.get(id=data_reason_code)
        self.obj.update({
            "reason_code": reason_code.id
        })
        return reason_code
    
    def location(self, data):
        location = self.fk_models_serializer['location'][0].objects.get(id=data['location'])
        self.obj.update({
            "location": location.id,
            "branch": location.branch_group_id
        })
        return location

    def price_list(self, data):
        price_list = self.fk_models_serializer['price_list'][0].objects.get(id=data["price_list"])
        self.obj.update({
            "price_list": price_list.id
        })
        return price_list

    def validate_item_group(self, data):
        item_group = self.fk_models_serializer['item_group'][0].objects.get(id=data["item_group"])
        if item_group.item_group_name == 'Asset':
            if not data["fixed_asset_group"]:
                raise Exception ("Please specify Fixed Asset Group")
            else:
                fixed_asset_group = FixedAssetGroup.objects.get(id=data['fixed_asset_group'])
                
                self.obj.update({
                    "item_group": item_group.id,
                    "fixed_asset_group": fixed_asset_group.id
                })
                return item_group, fixed_asset_group
        
        self.obj.update({
            "item_group": item_group.id
        })
        
        return item_group


    # set total amount items table
    # note: rate should be calculated with VAT
    def set_poitems_obj(self, items):
        items_table = []
        total = 0
        net_amount = 0
        for i in items:
            total += i['amount']
            net_amount += i['amount_payable']
            obj = {
                "item": i['item_id'],
                "item_code": i['code'],
                "item_shortname": i['item_shortname'],
                "qty": i['qty'],
                "uom": i['uom_id'],
                "rate": i['rate'],
                "amount": i['amount'],
                "gross_rate": i['gross_rate'],
                "net_rate": i['net_rate'],
                "amount_payable": i['amount_payable'],
                "vat_amount": i['vat_amount'],
                "vat_group": i['vat_group_id']
            }

            items_table.append(obj)

        # totals
        self.net_amount = net_amount
        self.total_amount = total

        self.obj.update({
            "total_amount": total,
            "net_amount": net_amount
        })

        return items_table

        

