from django.db import models
from accounting.docs.price_list.price_list_model import PriceList
from stock.docs.item.item_model import Item
from buying.docs.supplier.supplier_model import Supplier
from stock.docs.uom.uom_model import UOM

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class ItemPrice(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, default="ITM-PRC_{9}")   ## system generated
    rate = models.DecimalField(decimal_places=2, max_digits=10)
    #FK
    base_uom = models.ForeignKey(UOM, models.CASCADE, null=True)
    price_list = models.ForeignKey(PriceList, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, models.CASCADE, null=True)
    
    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)