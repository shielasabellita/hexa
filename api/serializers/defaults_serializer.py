from typing import ChainMap
from rest_framework import serializers
from api.models import Company, AccountingPeriod, StatusAndRCode
from api.models.settings_model import ChartOfAccounts


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_code', 'company_name', 'company_shortname', 'company_address',
        'company_contact_no', 'company_email', 'is_group', 'company_group',
        'currency', 'company_reg_no', 'company_taxid_no', 'business_permit_no',
        'created_at', 'updated_at', 'deleted_at']


class AccountingPeriodSerializer(serializers.ModelSerializer):
    company_id = serializers.RelatedField(source='company.company_code', read_only=True)
    class Meta:
        model = AccountingPeriod
        fields = ['id', 'acctng_period_code', 'acctng_period_name', 'acctng_period_start_date',
                'acctng_period_end_date', 'status', 'company_id',
                'created_at', 'updated_at', 'deleted_at']


class StatusAndReasonCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusAndRCode
        fields = ['id', 'module_group', 'module', 'sub_module', 
                'trans_type', 'trans_label', 'trans_label_shortname', 
                'trans_trigger', 'remarks', 'created_at', 'updated_at', 'deleted_at']


class ChartOfAccountsSerializer(serializers.ModelSerializer):
    company_id = serializers.RelatedField(source='company.company_code', read_only=True)
    class Meta:
        model = ChartOfAccounts
        fields = ['id', 'account_code', 'account_name', 'account_type_and_financial_group', 'normal_balance',
                'company_id','report', 'is_default_expense', 'created_at', 'updated_at', 'deleted_at']