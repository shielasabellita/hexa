from django.db import models
from accounting.docs.pricing_rule.pricing_rule_model import PricingRule

from buying.docs.item_receipt.item_receipt_model import ItemReceipt
from stock.models import *
from accounting.models import VatGroup


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class IRItems(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True, default="IR-ITM_{10}")  ## system generated

    has_uom_variance = models.CharField(choices=GLOBAL_YES_NO, default=0, max_length=1)

    # item
    item = models.ForeignKey(Item, on_delete=models.CASCADE) # FK
    item_code = models.CharField(max_length=120, blank=True)
    item_name = models.CharField(max_length=120, blank=True)
    item_shortname = models.CharField(max_length=120, blank=True)
    # qty
    qty_ordered = models.FloatField(max_length=10, default=0)
    qty_received = models.FloatField(max_length=10, default=0)
    qty_over = models.FloatField(max_length=10, default=0)

    # uom
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE) # FK
    uom_name = models.CharField(max_length=120, blank=True)
    
    # amount
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # net
    gross_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_payable = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # fks
    vat_group = models.ForeignKey(VatGroup, on_delete=models.CASCADE, null=True)
    price_rule = models.ForeignKey(PricingRule, on_delete=models.CASCADE, null=True) # FK

    # parent
    item_receipt = models.ForeignKey(ItemReceipt, on_delete=models.CASCADE)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)