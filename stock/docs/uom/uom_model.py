from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class UOM(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated
    uom = models.CharField(max_length=120)
    must_be_a_whole_number = models.IntegerField(choices=GLOBAL_YES_NO, default=0)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)