from django.db import models
from accounting.docs.cost_center.cost_center_model import CostCenter
from accounting.docs.vat_group.vat_group_model import VatGroup
from accounting.docs.withholding_tax_group.withholding_tax_model import WithHoldingTaxGroup
from accounting.docs.price_list.price_list_model import PriceList
from accounting.docs.chart_of_accounts.chart_of_accounts_model import ChartOfAccounts

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class Customer(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated

    cust_name = models.CharField(max_length=120)
    cust_shortname = models.CharField(max_length=120, blank=True)
    tax_identification_no = models.CharField(max_length=120, blank=True)
    term = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=120, blank=True)
    street = models.CharField(max_length=120, blank=True)
    brgy = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    province = models.CharField(max_length=120, blank=True)
    postal_code = models.CharField(max_length=120, blank=True)
    customer_group = models.CharField(max_length=120, blank=True)
    #FK
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE, null=True)
    vat_group = models.ForeignKey(VatGroup, on_delete=models.CASCADE, null=True)
    wht = models.ForeignKey(WithHoldingTaxGroup, on_delete=models.CASCADE, null=True)
    default_pricelist = models.ForeignKey(PriceList, on_delete=models.CASCADE, null=True)
    default_receivable_account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, null=True)


    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)