from django.db import models
from accounting.docs.price_list.price_list_model import PriceList

from stock.models import *
from setup.models import *
from buying.models import *
from accounting.models import CostCenter


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class PurchaseOrder(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, default="PO_{7}")   ## system generated

    reason_code = models.ForeignKey(StatusAndRCode, on_delete=models.CASCADE, null=True) # FK
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE, null=True) # FK
    fixed_asset_group = models.ForeignKey(FixedAssetGroup, on_delete=models.CASCADE, null=True) # FK
    
    date = models.DateField(auto_now_add=True)
    date_expected = models.DateField(auto_now_add=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True) # FK
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE, null=True) # FK
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True) # FK
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True) # FK
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, null=True) # FK

    total_amount = models.DecimalField(decimal_places=4, max_digits=10, default=0)
    net_amount = models.DecimalField(decimal_places=4, max_digits=10, default=0)
    
    apply_tax = models.CharField(choices=GLOBAL_YES_NO, default=0, max_length=1)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)