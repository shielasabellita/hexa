from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class PriceList(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    code = models.CharField(max_length=120, default="PR-LST_{5}")   ## system generated
    
    price_list_name = models.CharField(max_length=120)
    is_buying = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    is_selling = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    is_transfer = models.IntegerField(choices=GLOBAL_YES_NO, default=0)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)