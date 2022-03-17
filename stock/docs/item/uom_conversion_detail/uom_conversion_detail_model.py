from django.db import models
from accounting.docs.price_list.price_list_model import PriceList
from stock.docs.uom.uom_model import UOM

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class UOMConversionDetail(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated
    conversion_factor = models.FloatField()
    #FK
    uom = models.ForeignKey(UOM, models.CASCADE, null=True)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    
    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)