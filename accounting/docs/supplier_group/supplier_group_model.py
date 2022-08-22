from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class SupplierGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    code = models.CharField(max_length=120, default="SUP-GRP_{5}")   ## system generated
    supplier_group = models.CharField(max_length=120)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)