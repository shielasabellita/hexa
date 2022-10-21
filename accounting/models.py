from django.db import models
from accounting.docs.chart_of_accounts.chart_of_accounts_model import ChartOfAccounts
from accounting.docs.cost_center.cost_center_model import CostCenter
from accounting.docs.discount_group.discount_rate_model.discount_rate_model import DiscountRate
from accounting.docs.price_list.price_list_model import PriceList
from accounting.docs.supplier_group.supplier_group_model import SupplierGroup
from accounting.docs.vat_group.vat_group_model import VatGroup
from accounting.docs.withholding_tax_group.withholding_tax_model import WithHoldingTaxGroup
from accounting.docs.discount_group.discount_group_model import DiscountGroup
from accounting.docs.pricing_rule.pricing_rule_model import PricingRule
from accounting.docs.pricing_rule.pricing_rule_apply_to.apply_to_item_supplier_model import ApplyTo
from accounting.docs.discount_group.discount_items.discount_items_model import DiscountItems

## docs/chart_of_accounts
ChartOfAccounts()

## docs/cort_Center
CostCenter()

## docs/PriceList
PriceList()


## docs/suppleir_group
SupplierGroup()

## docs/vat_group
VatGroup()

## docs/withholding_tax
WithHoldingTaxGroup()

## docs/discount group
DiscountGroup()

PricingRule()

ApplyTo()

DiscountItems()

DiscountRate()