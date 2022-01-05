from typing import Tuple
from django.db import models


GLOBAL_YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
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
    is_buying = models.CharField(max_length=4, default='No', choices=GLOBAL_YES_NO)
    is_selling = models.CharField(max_length=4, default='No', choices=GLOBAL_YES_NO)
    is_both = models.CharField(max_length=4, default='No', choices=GLOBAL_YES_NO)