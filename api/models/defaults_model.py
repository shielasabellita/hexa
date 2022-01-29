from typing import Tuple
from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class StatusAndRCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_group = models.CharField(max_length=120)
    module = models.CharField(max_length=120)
    sub_module = models.CharField(max_length=120)
    trans_type = models.CharField(max_length=120)
    trans_label = models.CharField(max_length=120)
    trans_label_shortname = models.CharField(max_length=120)
    trans_trigger = models.CharField(max_length=100)
    remarks = models.CharField(max_length=120)


class PriceList(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    is_buying = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    is_selling = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    is_transfer = models.IntegerField(choices=GLOBAL_YES_NO, default=0)


# class ItemGroup(models.Model):
#     id = models.CharField(max_length=120, primary_key=True)
#     item_groupname = models.CharField(max_length=120)
#     fixed_asset_group = models.CharField(max_length=120)
#     vat_group = models.CharField(max_length=120)
#     default_income = models.CharField(max_length=120)
#     default_cos_account = models.CharField(max_length=120)
