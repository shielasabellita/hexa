from django.db import models
from setup.docs.company.company_model import Company

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

STATUS = (
        ("Open", "Open"),
        ("Closed", "Closed"),
    )

class AccountingPeriod(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    code = models.CharField(max_length=45, blank=True) ## system generated
    acctng_period_name = models.CharField(max_length=45, blank=True)
    acctng_period_start_date = models.DateField(blank=True)
    acctng_period_end_date = models.DateField(blank=True)
    status = models.CharField(max_length=45, default="Open", choices=STATUS)

    # monthly
    jan = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    feb = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    mar = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    apr = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    may = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    jun = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    jul = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    aug = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    sep = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    oct = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    nov = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    dec = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    
    # foreign key
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)