from typing import Tuple
from django.db import models

class VatGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    vat_group_code = models.CharField(max_length=120)
    vat_group_name = models.CharField(max_length=120)
    rate = models.CharField(max_length=120)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class WithHoldingTaxGroup(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    wht_code = models.CharField(max_length=120)
    wht_name = models.CharField(max_length=120)
    rate = models.CharField(max_length=120)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)