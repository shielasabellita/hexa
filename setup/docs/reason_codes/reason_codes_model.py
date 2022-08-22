from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class StatusAndRCode(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    code = models.CharField(max_length=120, default="RC_{9}")   ## system generated
    
    module_group = models.CharField(max_length=120)
    module = models.CharField(max_length=120)
    sub_module = models.CharField(max_length=120)
    trans_type = models.CharField(max_length=120)
    trans_label = models.CharField(max_length=120)
    trans_label_shortname = models.CharField(max_length=120)
    trans_trigger = models.CharField(max_length=100)
    remarks = models.CharField(max_length=120)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)