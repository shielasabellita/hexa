from typing import Tuple
from django.db import models




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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)