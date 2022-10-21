from django.db import models
from accounting.docs.discount_group.discount_group_model import DiscountGroup
from stock.models import Item

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class DiscountItems(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, default="DISC-ITMS_{9}")   ## system generated

    item = models.ForeignKey(Item, models.CASCADE)
    disc_group = models.ForeignKey(DiscountGroup, models.CASCADE)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)