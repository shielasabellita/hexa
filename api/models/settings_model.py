from typing import Tuple
from django.db import models

# Create your models here.



class Company(models.Model):
    company_code = models.CharField(max_length=50, primary_key=True)
    company_name = models.CharField(max_length=50)
    company_shortname = models.CharField(max_length=50)
    company_address = models.CharField(max_length=50, null=True)
    company_contact_no = models.CharField(max_length=50, null=True)
    company_email = models.CharField(max_length=50, null=True)
    is_group = models.BooleanField(default=0)
    company_group = models.CharField(max_length=50, null=True)
    currency = models.CharField(max_length=4, default="PHP")
    company_reg_no = models.CharField(max_length=50, null=True)
    company_taxid_no = models.CharField(max_length=50, null=True)
    business_permit_no = models.CharField(max_length=50, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    deleted_at = models.DateField(auto_now=True, blank=True)


class AccountingPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    acctng_period_code = models.CharField(max_length=45)
    acctng_period_name = models.CharField(max_length=45)
    acctng_period_start_date = models.DateField()
    acctng_period_end_date = models.DateField()
    status = models.CharField(max_length=45, default="Open")

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    deleted_at = models.DateField(auto_now=True, blank=True)
    # foreign key
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)


class Branch(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_code = models.CharField(max_length=45)
    branch_name = models.CharField(max_length=45)
    branch_shortname = models.CharField(max_length=45)
    is_group = models.BooleanField(default=0)
    company_group = models.CharField(max_length=45)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    deleted_at = models.DateField(auto_now=True, blank=True)
    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    

class ChartOfAccounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_code = models.CharField(max_length=50)
    account_name = models.CharField(max_length=50)
    account_type_and_financial_group = models.CharField(max_length=80)
    normal_balance = models.CharField(max_length=50)
    report = models.CharField(max_length=50)
    is_default_expense = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    deleted_at = models.DateField(auto_now=True, blank=True)

    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    

class CostCenter(models.Model):
    id = models.BigAutoField(primary_key=True)
    cost_center_code = models.CharField(max_length=50)
    cost_center_name = models.CharField(max_length=50)
    cost_center_shortname = models.CharField(max_length=50)
    is_group = models.BooleanField(default=0)
    cost_center_group = models.CharField(max_length=50)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    deleted_at = models.DateField(auto_now=True, blank=True)
    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_code = models.CharField(max_length=50)
    location_name = models.CharField(max_length=50)
    location_shortname = models.CharField(max_length=50)
    is_group = models.BooleanField(default=0)
    branch_group = models.CharField(max_length=50, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    deleted_at = models.DateField(auto_now=True, blank=True)
    # FK
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    
