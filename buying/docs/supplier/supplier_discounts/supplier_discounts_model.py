from pyexpat import model
from django.db import models
from buying.docs.supplier.supplier_model import Supplier
from accounting.docs.discount_group.discount_group_model import DiscountGroup



class SupplierDiscounts(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated
    
    # FK
    supplier = models.ForeignKey(Supplier, models.CASCADE, null=True)
    discount_group = models.ForeignKey(DiscountGroup, models.CASCADE, null=True)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)