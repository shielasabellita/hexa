from django.db import models
from accounting.docs.cost_center.cost_center_model import CostCenter
from setup.docs.location.location_model import Location


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

employment_type = (
    ("Direct Hire", "Direct Hire"),
    ("Agency", "Agency"),
    ("Job Order", "Job Order"),
    ("On Call", "On Call"),
)

gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class Employee(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)   ## system generated
    
    emp_name = models.CharField(max_length=120)
    is_custodian = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    is_driver = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    employment_type = models.CharField(max_length=120, choices=employment_type)
    gender = models.CharField(max_length=120, choices=gender)
    birthday = models.DateField(blank=True)
    contact_no = models.CharField(max_length=120, blank=True)
    date_of_joining = models.DateField(blank=True, null=True)
    date_of_separation = models.DateField(blank=True, null=True)
    is_active = models.IntegerField(choices=GLOBAL_YES_NO, default=1)
    emergency_contact_name = models.CharField(max_length=120, blank=True)
    emergency_contact_no = models.CharField(max_length=120, blank=True)
    relation = models.CharField(max_length=120, blank=True)
    daily_wage = models.CharField(max_length=120, blank=True)
    is_minimum_wage = models.IntegerField(choices=GLOBAL_YES_NO, default=0)
    
    
    # FK
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)