from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document
from stock.docs.item.item_model import Item
from stock.docs.uom.uom_model import UOM

from .purchase_order_serializer import PurchaseOrderSerializer, PurchaseOrder

from accounting.docs.price_list.price_list_serializer import PriceListSerializer, PriceList
from accounting.docs.cost_center.cost_center_serializer import CostCenterSerializer, CostCenter
from setup.docs.branch.branch_serializer import Branch, BranchSerializer
from setup.docs.location.location_serializer import LocationSerializer, Location
from stock.docs.item_group.item_group_serializer import ItemGroupSerializer, ItemGroup
from setup.docs.reason_codes.reason_codes_serializer import StatusAndRCodeSerializer, StatusAndRCode
from stock.docs.fixed_asset_group.fixed_asset_serializer import FixedAssetGroupSerializer, FixedAssetGroup
from buying.docs.supplier.supplier_serializer import Supplier, SupplierSerializer
from .po_items.po_items_model import POItems

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
    
    obj = {}
    
    def __init__(self, *args, **kwargs):
        args = (PurchaseOrder, PurchaseOrderSerializer)
        super().__init__(*args,**kwargs)

    ## REQUEST - POST
    def post(self, request):
        data = request.data
        self.set_obj_data(data)
        
        









    def set_obj_data(self, data):
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


    
    # items
    # def 

    
    

