from django.db import models

GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )



class Employee(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    uom = models.CharField(max_length=120)
    must_be_a_whole_number = models.IntegerField(choices=GLOBAL_YES_NO, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)