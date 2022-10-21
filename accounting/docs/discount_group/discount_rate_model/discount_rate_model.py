from email.policy import default
from django.db import models
from accounting.docs.discount_group.discount_group_model import DiscountGroup

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class DiscountRate(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, default="DISC-RATE_{9}")   ## system generated

    disc_rate = models.FloatField()
    disc_name = models.CharField(max_length=120)
    disc_group = models.ForeignKey(DiscountGroup, models.CASCADE)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)