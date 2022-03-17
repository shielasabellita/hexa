from rest_framework import serializers
from .accounting_period_model import AccountingPeriod

class AccountingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingPeriod
        fields = "__all__"