from django.db import models
from accounting.docs.pricing_rule.pricing_rule_model import PricingRule

from buying.docs.purchase_order.purchase_order_model import PurchaseOrder
from stock.models import *
from accounting.models import VatGroup

class POItems(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True, default="PO-ITM_{10}")  ## system generated

    item = models.ForeignKey(Item, on_delete=models.CASCADE) # FK
    item_description = models.CharField(max_length=120, blank=True)
    item_shortname = models.CharField(max_length=120, blank=True)
    qty_ordered = models.FloatField(max_length=10, default=0)
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE) # FK
    rate = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    vat_group = models.ForeignKey(VatGroup, on_delete=models.CASCADE, null=True)
    price_rule = models.ForeignKey(PricingRule, on_delete=models.CASCADE, null=True) # FK

    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)