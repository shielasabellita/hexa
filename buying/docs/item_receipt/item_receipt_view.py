import json
from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document
from stock.docs.item.item_model import Item
from stock.docs.uom.uom_model import UOM

from .item_receipt_serializer import ItemReceipt, ItemReceiptSerializer
from .ir_items.ir_items_serializer import IRItems, IRItemsSerializer

from accounting.docs.price_list.price_list_serializer import PriceListSerializer, PriceList
from accounting.docs.cost_center.cost_center_serializer import CostCenterSerializer, CostCenter
from setup.docs.branch.branch_serializer import Branch, BranchSerializer
from setup.docs.location.location_serializer import LocationSerializer, Location
from stock.docs.item_group.item_group_serializer import ItemGroupSerializer, ItemGroup
from setup.docs.reason_codes.reason_codes_serializer import StatusAndRCodeSerializer, StatusAndRCode
from stock.docs.fixed_asset_group.fixed_asset_serializer import FixedAssetGroupSerializer, FixedAssetGroup
from buying.docs.supplier.supplier_serializer import Supplier, SupplierSerializer
# from .po_items.po_items_model import POItems

from controller.utils import get_percent, flt
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
# utils
from controller.controllers.transaction import validate_price_list, validate_item_group
from controller.controllers.buying import validate_date_and_request_date
from controller.controllers.item import _get_transaction_details


# class PurchaseOrderView(Document):
#     fk_fields = [
#             "reason_code", "item_group", "fixed_asset_group", 
#             "supplier", "cost_center", "branch", "location", "price_list"
#             ]

#     fk_models_serializer = {
#             "supplier": [Supplier, SupplierSerializer], 
#             "reason_code": [StatusAndRCode, StatusAndRCodeSerializer], 
#             "item_group": [ItemGroup, ItemGroupSerializer], 
#             "fixed_asset_group": [FixedAssetGroup, FixedAssetGroupSerializer], 
#             "supplier": [Supplier, SupplierSerializer], 
#             "cost_center": [CostCenter, CostCenterSerializer], 
#             "branch": [Branch, BranchSerializer], 
#             "location": [Location, LocationSerializer], 
#             "price_list": [PriceList, PriceListSerializer]
#         }
    
#     poitems_doc = POItemsView(POItems, POItemsSerializer)
    
#     obj = {}
#     net_amount = 0
#     total_amount = 0
#     items = []
    
#     def __init__(self, *args, **kwargs):
#         args = (PurchaseOrder, PurchaseOrderSerializer)
#         super().__init__(*args,**kwargs)

#     # API - GET
#     def get(self, request, *args, **kwargs):
#         try:
#             if request.GET.get('filters', None):
#                 data = self.get_filtered_list(json.loads(request.GET.get("filters")))
#             else:
#                 id = request.GET.get('id', None)
#                 data = self.get_data(id=id)

#             return Response(data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#     def get_data(self, id=None, filters=None):
#         data = {}
#         if filters:
#             data = self.get_list(filters=filters, fk_fields=self.fk_fields, models_serializer=self.fk_models_serializer)
#             for d in data:
#                 d.update(self.get_child_data(d['id']))

#             return data

#         if id or not id:
#             data = self.get_list(id, fk_fields=self.fk_fields, models_serializer=self.fk_models_serializer)
#             if data:
#                 if isinstance(data, ReturnDict):
#                     data.update(self.get_child_data(data['id']))
#                 elif isinstance(data, ReturnList):
#                     for d in data:
#                         d.update(self.get_child_data(d['id'])) 

#             return data
        
        
#     def get_all_data(self):
#         return self.get_data()
    
#     def get_filtered_list(self, filters):
#         return self.get_data(filters=filters)

#     def get_child_data(self, parent):
#         obj = {
#             "items": self.poitems_doc.get_list(filters={"purchase_order": parent})
#         }
#         return obj


#     # API - POST
#     def post(self, request):
#         data = request.data
        
#         try:
#             self.set_po_obj(data)
#             self.validate_items_and_total(data)

#             if not data.get('items'):
#                 raise Exception("Missing Items")

#             serialized_po_data = self.create(self.obj, user=str(request.user))
#             serialized_po_data.update({
#                 "items": []
#             })
#             if serialized_po_data:
#                 po_doc = PurchaseOrder.objects.get(id=serialized_po_data['id'])
#                 for itm in self.obj.get('items'):
#                     itm.update({
#                         "purchase_order": po_doc.id,
#                     })
                    
#                     po_item_data = self.poitems_doc.create(data=itm, user=str(request.user))
#                     serialized_po_data['items'].append(po_item_data)
            
#             # return formatted data
#             dt = self.get_data(id=serialized_po_data.get("id"))
#             return Response(dt)
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#     def set_po_obj(self, data):
#         # set PO Data for creationg
#         self.obj = data
#         def set_location_branch(data):
#             # fetch branch from selected location
#             location = self.fk_models_serializer['location'][0].objects.get(id=data['location'])
#             self.obj.update({
#                 "branch": location.branch_group.id
#             })
        
#         set_location_branch(data)
#         validate_date_and_request_date(data.get('date'), data.get('date_expected'))
#         validate_price_list(data.get("price_list"), type='Purchasing')

#         item_group = validate_item_group(data.get("item_group"), data.get("fixed_asset_group", None))
#         if len(item_group) == 2:
#             self.obj.update({
#                 "fixed_asset_group": item_group[1].id
#             })

#     # set total amount items table
#     # note: rate should be calculated with VAT
#     # used to create or update
#     def validate_items_and_total(self, data, method="create"):
#         new_dt = _get_transaction_details(data, method)
#         items = []
#         for i in new_dt.get("items"): 
#             item_obj = {
#                 "item": i['item'],
#                 "item_code": i['item_code'],
#                 "item_name": i['item_name'],
#                 "item_shortname": i['item_shortname'],
#                 "qty": i['qty'],
#                 "uom": i['uom'],
#                 "uom_name": i['uom_name'],
#                 "rate": i['rate'],
#                 "amount": i['amount'],
#                 "gross_rate": i['gross_rate'],
#                 "net_rate": i['net_rate'],
#                 "amount_payable": i['amount_payable'],
#                 "vat_amount": i['vat_amount'],
#                 "vat_group": i['vat_group']
#             }

#             if method == 'update':
#                 item_obj.update({
#                     "id": i['id']
#                 })

#             items.append(item_obj)

#         self.obj.update({
#             "items": items,
#             "net_total": new_dt['net_total'],
#             "total_amount": new_dt['total_amount']
#         })

        
#     # API - DELETE
#     def delete(self, request, *args, **kwargs):
#         ids = request.data['ids']
#         for id in ids: 
#             try:
#                 self.remove(id, "Purchase Order", request.user)
#             except Exception as e:
#                 return Response("Error on ID {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         return Response("Successfully deleted", status=status.HTTP_200_OK)


#     # API - UPDATE
#     def put(self, request, *args, **kwargs):
#         data = request.data
#         self.get_val(data.get("id"))

#         if not data.get('items', None):
#             raise Exception("Missing Items")

#         try:
#             self.set_po_obj(data)
#             self.validate_items_and_total(data, method='update')

#             serialized_data = self.update(id=data.get("id"), data=self.obj, user=str(request.user))
#             if serialized_data: 
#                 serialized_data.update({"items": []})
#                 for itm in self.obj.get("items"):
#                     itm.update({
#                         "purchase_order": data.get("id")
#                     })
#                     po_item_data = self.poitems_doc.update(id=itm.get("id"), data=itm, user=str(request.user))
#                     serialized_data['items'].append(po_item_data)

#             # return formatted data
#             dt = self.get_data(id=data.get("id"))
#             return Response(dt)
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
