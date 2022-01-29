from django.db import models
from api.models.accounting import *
from api.models.stock import *
from api.models.buying import *
from api.models.setup_model import *
from api.models.system_model import *
from api.models.defaults_model import *


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

    is_purchase_item = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    # fk
    purchase_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, default="Unit", related_name="purchase_uom")
    
    is_sales_item = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    # fk
    sales_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, default="Unit", related_name="sales_uom")

    #FK
    base_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, default="Unit")
    item_group = models.ForeignKey(
                ItemGroup, 
                on_delete=models.CASCADE, 
                related_name="item_group", 
                default="Product")

    fixed_asset_group = models.ForeignKey(
                ItemGroup, 
                on_delete=models.CASCADE, 
                null=True, 
                related_name="fixed_asset_group")

    vat_group = models.ForeignKey(
                VatGroup, 
                on_delete=models.CASCADE, 
                null=True, 
                related_name="vat_group")

    default_income_account = models.ForeignKey(
                ChartOfAccounts, 
                on_delete=models.CASCADE, 
                null=True, 
                related_name="default_income_account")
                
    default_cos_account = models.ForeignKey(
                ChartOfAccounts, 
                on_delete=models.CASCADE, 
                null=True, 
                related_name="default_cos_account")



class ItemPrice(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    price = models.FloatField(default=0.00)

    base_uom = models.ForeignKey(UOM, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)



## ITEM CHILD TABLES
class UOMConversionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    conversion_factor = models.FloatField()
    
    #FK
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)








