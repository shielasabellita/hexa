from django.db import models

# Create your models here.

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class ParentCompany(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, default="PRNT-COMP_{5}")  ## system generated
    parent_company_name = models.CharField(max_length=120)
     
    
    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)