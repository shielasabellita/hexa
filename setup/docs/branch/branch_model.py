from django.db import models
from setup.docs.company.company_model import Company


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class Branch(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=45, blank=True)     ## system generated
    branch_name = models.CharField(max_length=45)
    branch_shortname = models.CharField(max_length=45)
    is_group = models.IntegerField(choices=GLOBAL_YES_NO, default=0)

    # foreign key
    company_group = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
