from pyexpat import model
from django.db import models
from selling.docs.customer.customer_model import Customer
from accounting.docs.discount_group.discount_group_model import DiscountGroup



class CustomerDiscounts(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, default="CUST-DISC_{9}")   ## system generated
    
    # FK
    customer = models.ForeignKey(Customer, models.CASCADE, null=True)
    discount_group = models.ForeignKey(DiscountGroup, models.CASCADE, null=True)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)