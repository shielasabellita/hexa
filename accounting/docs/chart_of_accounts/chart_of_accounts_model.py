from django.db import models


GLOBAL_YES_NO = (
        (1, 1),
        (0, 0),
    )


class ChartOfAccounts(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    code = models.CharField(max_length=120, default="COA_{5}")   ## system generated

    account_code = models.CharField(max_length=120, blank=True)
    account_name = models.CharField(max_length=120)
    account_type_and_financial_group = models.CharField(max_length=80, blank=True)
    normal_balance = models.CharField(max_length=120, blank=True)
    report = models.CharField(max_length=120, blank=True)
    is_default_expense = models.IntegerField(choices=GLOBAL_YES_NO, default=0)

    # defaults
    created_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

