from django.db import models
from buying.docs.supplier.supplier_model import Supplier 
from buying.docs.supplier.supplier_discounts.supplier_discounts_model import SupplierDiscounts
from buying.docs.purchase_order.po_items.po_items_model import POItems
from buying.docs.purchase_order.purchase_order_model import PurchaseOrder

from buying.docs.item_receipt.ir_items.ir_items_model import ItemReceipt, IRItems

# supplier
Supplier()

# supplier -> supplier discounts
SupplierDiscounts()

# PO
PurchaseOrder()
# PO -> Items
POItems()

# IR 
ItemReceipt()
# IR -> IR Items
IRItems()