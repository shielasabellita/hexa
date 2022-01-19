from functools import cmp_to_key
from django.db import models
from api.models.setup_model import CostCenter, ChartOfAccounts
from api.models.accounting.accounting_group_model import VatGroup, WithHoldingTaxGroup
from api.models.defaults_model import PriceList


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class SupplierGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)


class DiscountGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    discount_name = models.CharField(max_length=120)


class Supplier(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    sup_code = models.CharField(max_length=120)
    sup_name = models.CharField(max_length=120)
    sup_shortname = models.CharField(max_length=120, blank=True)
    check_payee_name = models.CharField(max_length=120, blank=True)
    is_trucker = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    tax_identification_no = models.CharField(max_length=120, blank=True)
    term = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=120, blank=True)
    street = models.CharField(max_length=120, blank=True)
    brgy = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    province = models.CharField(max_length=120, blank=True)
    postal_code = models.CharField(max_length=120, blank=True)

    #foreign keys
    supplier_group = models.ForeignKey(SupplierGroup, on_delete=models.CASCADE)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE, blank=True)
    vat_group = models.ForeignKey(VatGroup, on_delete=models.CASCADE, blank=True)
    wht = models.ForeignKey(WithHoldingTaxGroup, on_delete=models.CASCADE, blank=True)
    discount_group1 = models.ForeignKey(DiscountGroup, on_delete=models.CASCADE, blank=True, related_name='discount1')
    discount_group2 = models.ForeignKey(DiscountGroup, on_delete=models.CASCADE, blank=True, related_name='discount2')
    discount_group3 = models.ForeignKey(DiscountGroup, on_delete=models.CASCADE, blank=True, related_name='discou')
    default_pricelist = models.ForeignKey(PriceList, on_delete=models.CASCADE, blank=True)
    default_expense_account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, blank=True)
    
    # defaults fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)