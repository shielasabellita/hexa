from rest_framework import serializers
from api.models import Company, AccountingPeriod, StatusAndRCode
from api.models.setup_model import ChartOfAccounts


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AccountingPeriodSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = AccountingPeriod
        fields = '__all__'


class StatusAndReasonCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusAndRCode
        fields = '__all__'

class ChartOfAccountsSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = ChartOfAccounts
        fields = '__all__'