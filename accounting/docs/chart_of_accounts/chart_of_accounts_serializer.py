from rest_framework import serializers
from .chart_of_accounts_model import ChartOfAccounts

class ChartOfAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccounts
        fields = "__all__"