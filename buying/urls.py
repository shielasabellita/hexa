from django.urls import path, include

from buying.docs.supplier.supplier_discounts.supplier_discounts_model import SupplierDiscounts
from .docs.supplier.supplier_view import SupplierView
from .docs.supplier.supplier_discounts.supplier_discounts_view import SupplierDiscountsView


urlpatterns = [
    # MD
    path("docs/supplier", SupplierView.as_view(), name='supplier'),
    path("docs/supplier_discounts", SupplierDiscountsView.as_view(), name='supplier_discounts'),
]