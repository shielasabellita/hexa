from django.db import models
from accounting.docs.pricing_rule.pricing_rule_model import PricingRule

from purchase_order.purchase_order_serializer import PurchaseOrder, PurchaseOrderSerializer
from stock.models import *
from accounting.models import VatGroup

class POItems(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated

    item = models.ForeignKey(Item, on_delete=models.CASCADE) # FK
    qty_ordered = models.FloatField(max_length=10, default=0)
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE) # FK
    amount = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    vat_group = models.ForeignKey(VatGroup, on_delete=models.CASCADE, null=True)
    price_rule = models.ForeignKey(PricingRule, on_delete=models.CASCADE, null=True) # FK

