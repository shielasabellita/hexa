from typing import Tuple
from django.db import models


class StatusAndRCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_group = models.CharField(max_length=45)
    module = models.CharField(max_length=45)
    sub_module = models.CharField(max_length=45)
    trans_type = models.CharField(max_length=45)
    trans_label = models.CharField(max_length=45)
    trans_label_shortname = models.CharField(max_length=45)
    trans_trigger = models.CharField(max_length=45)
    remarks = models.CharField(max_length=45)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    deleted_at = models.DateField(auto_now=True, blank=True)