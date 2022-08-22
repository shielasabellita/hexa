from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class  DiscountGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, default="DISC-GRP_{9}")   ## system generated

    discount_name = models.CharField(max_length=120)
    discounts = models.CharField(max_length=120)
    total_discount = models.FloatField()


    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)