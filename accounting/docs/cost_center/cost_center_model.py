from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class CostCenter(models.Model):
    id = models.CharField(max_length=120,primary_key=True)
    code = models.CharField(max_length=120, default="CST-CNTR_{5}")   ## system generated
    
    cost_center_name = models.CharField(max_length=120)
    cost_center_shortname = models.CharField(max_length=120)
    is_group = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    cost_center_group = models.CharField(max_length=120, blank=True)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
