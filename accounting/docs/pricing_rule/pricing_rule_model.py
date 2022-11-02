from django.db import models
from setup.models import Branch, Location
from stock.models import UOM

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

APPLY_FOR = (
        ("Buying", "Buying"),
        ("Selling", "Selling"),
    )

APPLY_TO = (
        ("Item", "Item"),
        ("Supplier", "Supplier"),
        ("Customer", "Customer"),
    )

STATUS = (
        ("Open", "Open"),
        ("Closed", "Closed"),
    )

class PricingRule(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    code = models.CharField(max_length=120, default="PRC-RLE_{6}")   ## system generated

    price_rule_name = models.CharField(max_length=120, blank=True)
    description = models.CharField(max_length=120, blank=True)
    apply_for = models.CharField(choices=APPLY_FOR, default='Buying', max_length=10)
    apply_to = models.CharField(choices=APPLY_TO, max_length=20)
    
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True) #FK
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True) #FK

    # criteria section
    criteria_qty = models.FloatField(default=0)
    criteria_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, null=True) ## FK
    criteria_amt = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    criteria_prd_start = models.DateField(null=True)
    criteria_prd_end = models.DateField(null=True)

    # discount section
    discount_percentage = models.FloatField(default=0)
    discount_amt = models.DecimalField(decimal_places=2, max_digits=10)

    status = models.CharField(choices=STATUS, default="Open", max_length=10)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
