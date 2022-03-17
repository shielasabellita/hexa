from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class DiscountGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated
    discount_name = models.CharField(max_length=120)
    discount1 = models.FloatField()
    discount2 = models.FloatField()
    discount3 = models.FloatField()
    total_discount = models.FloatField()


    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)