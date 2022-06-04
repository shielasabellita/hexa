from accounting.docs.cost_center.cost_center_model import CostCenter
from accounting.docs.cost_center.cost_center_serializer import CostCenterSerializer
from buying.docs.purchase_order.purchase_order_model import PurchaseOrder
from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document

from purchase_order_serializer import PurchaseOrderSerializer

from accounting.docs.price_list.price_list_serializer import PriceListSerializer, PriceList
from setup.docs.branch.branch_serializer import Branch, BranchSerializer
from setup.docs.location.location_serializer import LocationSerializer, Location
from stock.docs.item_group.item_group_serializer import ItemGroupSerializer, ItemGroup
from setup.docs.reason_codes.reason_codes_serializer import StatusAndRCodeSerializer, StatusAndRCode
from stock.docs.fixed_asset_group.fixed_asset_serializer import FixedAssetGroupSerializer, FixedAssetGroup
from buying.docs.supplier.supplier_serializer import Supplier, SupplierSerializer



class PurchaseOrderView(Document):
    fk_fields = [
            "reason_code", "item_group", "fixed_asset_group", 
            "supplier", "cost_center", "branch", "location", "price_list"
            ]

    fk_models_serializer = {
            "reason_code": [StatusAndRCode, StatusAndRCodeSerializer], 
            "item_group": [ItemGroup, ItemGroupSerializer], 
            "fixed_asset_group": [FixedAssetGroup, FixedAssetGroupSerializer], 
            "supplier": [Supplier, SupplierSerializer], 
            "cost_center": [CostCenter, CostCenterSerializer], 
            "branch": [Branch, BranchSerializer], 
            "location": [Location, LocationSerializer], 
            "price_list": [PriceList, PriceListSerializer]
        }

    def __init__(self, *args, **kwargs):
        args = (PurchaseOrder, PurchaseOrderSerializer)
        super().__init__(*args,**kwargs)

    