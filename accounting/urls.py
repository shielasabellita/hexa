from django.urls import path, include

from accounting.docs.chart_of_accounts.chart_of_accounts_model import ChartOfAccounts
from accounting.docs.cost_center.cost_center_model import CostCenter
from accounting.docs.price_list.price_list_model import PriceList
from .docs.chart_of_accounts.chart_of_accounts_view import ChartOfAccountsView
from .docs.cost_center.cost_center_view import CostCenterView
from .docs.price_list.price_list_view import PriceListView
from .docs.vat_group.vat_group_view import VatGroupView
from .docs.withholding_tax_group.withholding_tax_view import WithHoldingTaxGroupView
# from .docs.reason_codes.reason_codes_view import ReasonCode



urlpatterns = [
    # MD
    path("docs/coa", ChartOfAccountsView.as_view(), name='coa'),
    path("docs/cost_center", CostCenterView.as_view(), name='cost_center'),
    path("docs/price_list", PriceListView.as_view(), name='price_list'),
    path("docs/vat_group", VatGroupView.as_view(), name='vat_group'),
    path("docs/wth_group", WithHoldingTaxGroupView.as_view(), name='wth_group'),
]