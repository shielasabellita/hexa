
from django.db import models
from api.models.setup_model import CostCenter, ChartOfAccounts
from api.models.accounting.accounting_group_model import VatGroup, WithHoldingTaxGroup
from api.models.defaults_model import PriceList
from api.models.stock import Item, UOM


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class SupplierGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)



class DiscountGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    discount_name = models.CharField(max_length=120)
    discount1 = models.FloatField()
    discount2 = models.FloatField()
    discount3 = models.FloatField()
    total_discount = models.FloatField()



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
    wht = models.ForeignKey(WithHoldingTaxGroup, on_delete=models.CASCADE, blank=True, null=True)
    default_pricelist = models.ForeignKey(PriceList, on_delete=models.CASCADE, blank=True, null=True)
    default_expense_account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, blank=True, null=True, related_name='default_expense_account')
    default_payable_account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, blank=True, null=True, related_name='default_payable_account')
    
    # defaults fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


# supplier items
class SupplierItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    # FK
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


# tag to supplier
class SupplierDiscounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    discount_group = models.ForeignKey(DiscountGroup, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

# item price per supplier
class ItemPrice(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    price = models.FloatField(default=0.00)

    base_uom = models.ForeignKey(UOM, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)