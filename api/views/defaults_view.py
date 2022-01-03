from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import Company, AccountingPeriod, StatusAndRCode, ChartOfAccounts

# serializers
from api.serializers import CompanySerializer, AccountingPeriodSerializer

# other plugins
import pandas as pd

# helpers
from api.utils.helpers import get_static_path, get_coa_csv_path, get_rcs_csv_path

class SetupDefaultsView(APIView):
    def post(self, request, format=None):
        data = request.data
        
        company = self.get_company(data['company']['company_code'])
        if not company: 
            company = Company(**data['company'])
            company.save()

        try:
            data['accounting_period'].update({
                "id": "{} - {}".format(data['accounting_period']['acctng_period_code'], company.company_code)
            })
            AccountingPeriod.objects.create(**data['accounting_period'], company=company)
            self.sync_coa(company)
            self.sync_reason_codes()

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, company_code):
        try:
            data = {"accounting_period": []}
            
            company = self.get_company(company_code)
            if company:
                company_serializer = CompanySerializer(company)
                data.update({
                    'company': company_serializer.data
                })

                acctng_prd = AccountingPeriod.objects.filter(company = company_code)
                for acc in acctng_prd:
                    data['accounting_period'].append(
                        AccountingPeriodSerializer(acc).data
                    )
            
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get_company(self, company_code):
        try:
            company = Company.objects.get(company_code = company_code)
            return company
        except Company.DoesNotExist:
            return None
            

    def sync_coa(self, company):
        coas = pd.read_csv(get_coa_csv_path()).to_dict('records')
        for coa in coas:

            coa.update({
                "id": "{} - {} - {}".format(coa['account_code'], coa['account_name'], company.company_code)
            })

            ChartOfAccounts.objects.create(**coa, company=company)

    def sync_reason_codes(self):
        rcs = pd.read_csv(get_rcs_csv_path(), keep_default_na=False).to_dict('records')
        for rc in rcs:
            StatusAndRCode.objects.create(**rc)