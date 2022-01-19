from django.db import models
from .item_category_model import UOM




class ItemGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)


class FixedAssetGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)


class Item(models.Model):
    id = models.CharField(max_length=120,  primary_key=True)
    item_code = models.CharField(max_length=120)
    sku_code = models.CharField(max_length=120)
    item_barcode = models.CharField(max_length=120)
    item_name = models.CharField(max_length=120)
    item_shortname = models.CharField(max_length=120)
    item_group = models.CharField(max_length=120)
    



class UOMConversionFactor(models.Model):
    id = models.BigAutoField(primary_key=True)
    conversion_factor = models.FloatField()
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE)
    item_code = models.ForeignKey(Item, on_delete=models.CASCADE)