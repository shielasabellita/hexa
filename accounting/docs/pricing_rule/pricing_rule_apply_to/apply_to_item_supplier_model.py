from django.db import models
from accounting.docs.pricing_rule.pricing_rule_model import PricingRule
from stock.models import Item
from buying.models import Supplier

class ApplyTo(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    code = models.CharField(max_length=120, default="APLY-PRC-RLE_{9}")   ## system generated

    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    pricing_rule = models.ForeignKey(PricingRule, on_delete=models.CASCADE)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)