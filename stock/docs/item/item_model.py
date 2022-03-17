from django.db import models
from stock.docs.uom.uom_model import UOM
from stock.docs.item_group.item_group_model import ItemGroup
from accounting.docs.vat_group.vat_group_model import VatGroup
from accounting.docs.chart_of_accounts.chart_of_accounts_model import ChartOfAccounts

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class Item(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated
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
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE, related_name="item_group", default="Product")
    fixed_asset_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE, null=True, related_name="fixed_asset_group")
    vat_group = models.ForeignKey(VatGroup, on_delete=models.CASCADE, null=True, related_name="vat_group")
    default_income_account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, null=True, related_name="default_income_account")
    default_cos_account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, null=True, related_name="default_cos_account")

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)