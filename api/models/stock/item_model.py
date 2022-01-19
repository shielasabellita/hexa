from statistics import mode
from django.db import models

from api.models.accounting.accounting_group_model import VatGroup
from .item_category_model import UOM

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


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
    is_fixed_asset = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    maintain_stock = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    serial_no = models.CharField(max_length=120, blank=True)
    batch_no = models.CharField(max_length=120, blank=True)
    expiry = models.DateField(blank=True)
    purchase_item = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    sales_item = models.IntegerField(choices=GLOBAL_YES_NO, default=1)


    # One is to Many entity
    conversion_detail = models.CharField(max_length=450, blank=True)
    supplier_items = models.CharField(max_length=450, blank=True)

    #FK
    base_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, default="Unit")
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE, related_name="item_group", default="Product")
    fixed_asset_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE, blank=True, related_name="fixed_asset_group")
    vat_group = models.ForeignKey(VatGroup, on_delete=models.CASCADE, blank=True, related_name="vat_group")

    



class UOMConversionFactor(models.Model):
    id = models.BigAutoField(primary_key=True)
    conversion_factor = models.FloatField()
    
    #FK
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE)
    item_code = models.ForeignKey(Item, on_delete=models.CASCADE)