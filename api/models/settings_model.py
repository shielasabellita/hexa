from typing import Tuple
from django.db import models

# Create your models here.

GLOBAL_YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

class Company(models.Model):
    company_code = models.CharField(max_length=120, primary_key=True)
    company_name = models.CharField(max_length=120)
    company_shortname = models.CharField(max_length=120)
    company_address = models.CharField(max_length=120, null=True)
    company_contact_no = models.CharField(max_length=120, null=True)
    company_email = models.CharField(max_length=120, null=True)
    is_group = models.CharField(max_length=4, choices=GLOBAL_YES_NO, default='No')
    company_group = models.CharField(max_length=120, null=True)
    currency = models.CharField(max_length=4, default="PHP")
    company_reg_no = models.CharField(max_length=120, null=True)
    company_taxid_no = models.CharField(max_length=120, null=True)
    business_permit_no = models.CharField(max_length=120, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    


class AccountingPeriod(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    acctng_period_code = models.CharField(max_length=45)
    acctng_period_name = models.CharField(max_length=45)
    acctng_period_start_date = models.DateField()
    acctng_period_end_date = models.DateField()
    status = models.CharField(max_length=45, default="Open")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    # foreign key
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Branch(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_code = models.CharField(max_length=45)
    branch_name = models.CharField(max_length=45)
    branch_shortname = models.CharField(max_length=45)
    is_group = models.CharField(max_length=4, choices=GLOBAL_YES_NO, default='No')
    company_group = models.CharField(max_length=45)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    

class ChartOfAccounts(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    account_code = models.CharField(max_length=120)
    account_name = models.CharField(max_length=120)
    account_type_and_financial_group = models.CharField(max_length=80)
    normal_balance = models.CharField(max_length=120)
    report = models.CharField(max_length=120)
    is_default_expense = models.CharField(max_length=4, choices=GLOBAL_YES_NO, default='No')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    

    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    

class CostCenter(models.Model):
    id = models.BigAutoField(primary_key=True)
    cost_center_code = models.CharField(max_length=120)
    cost_center_name = models.CharField(max_length=120)
    cost_center_shortname = models.CharField(max_length=120)
    is_group = models.CharField(max_length=4, choices=GLOBAL_YES_NO, default='No')
    cost_center_group = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_code = models.CharField(max_length=120)
    location_name = models.CharField(max_length=120)
    location_shortname = models.CharField(max_length=120)
    is_group = models.CharField(max_length=4, choices=GLOBAL_YES_NO, default='No')
    branch_group = models.CharField(max_length=120, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
