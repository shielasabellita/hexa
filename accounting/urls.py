from math import frexp
from django.urls import path, include

from .docs.chart_of_accounts.chart_of_accounts_view import ChartOfAccountsView
from .docs.cost_center.cost_center_view import CostCenterView
from .docs.price_list.price_list_view import PriceListView
from .docs.vat_group.vat_group_view import VatGroupView
from .docs.withholding_tax_group.withholding_tax_view import WithHoldingTaxGroupView
from .docs.discount_group.discount_group_view import DiscountGroupView
from .docs.supplier_group.supplier_group_view import SupplierGroupView

# from .docs.reason_codes.reason_codes_view import ReasonCode



urlpatterns = [
    # MD
    path("docs/coa", ChartOfAccountsView.as_view(), name='coa'),
    path("docs/cost_center", CostCenterView.as_view(), name='cost_center'),
    path("docs/price_list", PriceListView.as_view(), name='price_list'),
    path("docs/vat_group", VatGroupView.as_view(), name='vat_group'),
    path("docs/wth_group", WithHoldingTaxGroupView.as_view(), name='wth_group'),
    path("docs/discount_group", DiscountGroupView.as_view(), name='discount_group'),
    path("docs/supplier_group", SupplierGroupView.as_view(), name='supplier_group'),
]