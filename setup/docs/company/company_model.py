from django.db import models
from setup.docs.parent_company.parent_company_model import ParentCompany


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class Company(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)  ## system generated
    company_name = models.CharField(max_length=120)
    company_shortname = models.CharField(max_length=120)
    company_address = models.CharField(max_length=120, null=True)
    company_contact_no = models.CharField(max_length=120, null=True)
    company_email = models.CharField(max_length=120, null=True)
    is_group = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    currency = models.CharField(max_length=4, default="PHP")
    company_reg_no = models.CharField(max_length=120, null=True)
    company_taxid_no = models.CharField(max_length=120, null=True)
    business_permit_no = models.CharField(max_length=120, null=True)
    is_construction_company = models.IntegerField(choices=GLOBAL_YES_NO, default=0)

    # parent company
    company_group = models.ForeignKey(ParentCompany, on_delete=models.CASCADE ,null=True)


    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

