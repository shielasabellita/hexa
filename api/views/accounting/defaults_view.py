
from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import Company, AccountingPeriod, StatusAndRCode, ChartOfAccounts
from api.models.accounting.accounting_group_model import VatGroup
from api.models.stock.item_model import FixedAssetGroup, ItemGroup

# serializers
from api.serializers.accounting import CompanySerializer, AccountingPeriodSerializer

# other plugins
import pandas as pd

# helpers
from api.utils.helpers import get_static_path, get_coa_csv_path, get_rcs_csv_path
from api.views.accounting.company_view import CompanyView

class SetupDefaultsView(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        if self.validate_one_company() == True:
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
                self.sync_vatgroup()
                self.sync_fixed_asset_group()
                self.sync_itemgroup()

                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        else:
            return Response("Database already used", status=status.HTTP_403_FORBIDDEN)


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

    def validate_one_company(self):
        if len(Company.objects.all()) > 0:
            return False
        else:
            return True

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


    def sync_vatgroup(self):
        vat = [
                {
                    "id" :"0% VAT-Exempt",
                    "vat_group_code": "0% VAT-Exempt",
                    "vat_group_name": "VAT-Exempt",
                    "rate": 0
                }, 
                {
                    "id" :"0% Zero Rated",
                    "vat_group_code": "0% Zero Rated",
                    "vat_group_name": "Zero Rated",
                    "rate": 0
                }, 
                {
                    "id" :"12% Input Tax",
                    "vat_group_code": "12% Input Tax",
                    "vat_group_name": "Input Tax",
                    "rate": 12
                }, 
                {
                    "id" :"12% Output Tax",
                    "vat_group_code": "12% Output Tax",
                    "vat_group_name": "Output Tax",
                    "rate": 12
                }
            ]
        for v in vat: 
            VatGroup.objects.create(**v)

    
    def sync_itemgroup(self):
        item_groups = ["Product", "Asset", "Material", "Service", "Other"]
        for ig in item_groups:
            ItemGroup.objects.create(id=ig)

    
    def sync_fixed_asset_group(self):
        fas = ["Motor Vehicle", "Office Equipment", "Furniture and Fixture"]
        for fa in fas:
            FixedAssetGroup.objects.create(id=fa)
