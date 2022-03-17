from django.db import models
from setup.docs.branch.branch_model import Branch


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )

class Location(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    code = models.CharField(max_length=120, blank=True)    ## system generated
    location_name = models.CharField(max_length=120)
    location_shortname = models.CharField(max_length=120)
    is_group = models.IntegerField(choices=GLOBAL_YES_NO, default=0)

    # foreign key
    branch_group = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


