from django.urls import path, include

#views
from buying.docs.supplier.supplier_discounts.supplier_discounts_model import SupplierDiscounts
from .docs.supplier.supplier_view import SupplierView
from .docs.supplier.supplier_discounts.supplier_discounts_view import SupplierDiscountsView
from .docs.purchase_order.purchase_order_view import PurchaseOrderView

urlpatterns = [
    # MD
    path("docs/supplier", SupplierView.as_view(), name='supplier'),
    path("docs/supplier_discounts", SupplierDiscountsView.as_view(), name='supplier_discounts'),

    # transaction
    path("tr/purchase_order", PurchaseOrderView.as_view(), name='purchase_order'),
    
]