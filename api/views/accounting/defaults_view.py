
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
from api.models.buying.supplier_model import SupplierGroup
from api.models.defaults_model import PriceList
from api.models.setup_model import CostCenter
from api.models.stock.item_category_model import UOM
from api.models.stock.item_model import FixedAssetGroup, ItemGroup
from api.models.system_model import Series

# serializers
from api.serializers.accounting import CompanySerializer, AccountingPeriodSerializer

# other plugins
import pandas as pd

# helpers
from api.utils.helpers import get_static_path, get_coa_csv_path, get_rcs_csv_path
from api.views.accounting.company_view import CompanyView

class SetupDefaultsView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
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
                self.sync_uom()
                self.sync_series()
                self.sync_price_list()
                self.sync_supplier_group()
                self.sync_costcenter()

                return Response(CompanySerializer(company).data, status=status.HTTP_200_OK)
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
                "id": "{} - {}".format(coa['account_code'], coa['account_name'])
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

    def sync_uom(self):
        uoms = [
            {
                "id": "Unit",
                "uom": "Unit"
            },
            {
                "id": "Case",
                "uom": "Case"
            },
        ]
        for uom in uoms: 
            UOM.objects.create(**uom)


    def sync_series(self):
        series = [
            {
                "id": "ITM",
                "no_of_zeroes": 9,
                "current": 0
            },
            {
                "id": "SUP",
                "no_of_zeroes": 9,
                "current": 0
            },
            {
                "id": "CUS",
                "no_of_zeroes": 9,
                "current": 0
            },
            {
                "id": "EMP",
                "no_of_zeroes": 9,
                "current": 0
            },
            {
                "id": "BRC",
                "no_of_zeroes": 9,
                "current": 0
            },
            {
                "id": "DEP",
                "no_of_zeroes": 9,
                "current": 0
            },
        ]
        for s in series:
            Series.objects.create(**s)


    def sync_price_list(self):
        prices = [
            {
                "id": "Buying",
                "is_buying": 1,
                "is_selling": 0,
                "is_transfer": 0,
            },
            {
                "id": "Selling",
                "is_buying": 0,
                "is_selling": 1,
                "is_transfer": 0,
            },
            {
                "id": "Transfer",
                "is_buying": 0,
                "is_selling": 0,
                "is_transfer": 1,
            },
        ]

        for p in prices: 
            PriceList.objects.create(**p)


    def sync_supplier_group(self):
        groups = ["Local", "Service", "Concessionaire", "Intercompany", "Imported"]
        
        for g in groups:
            SupplierGroup.objects.create(id=g)


    def sync_costcenter(self):
        costcenter = [
            {
                "cost_center_name": "Administration",
                "cost_center_shortname": "AD",
            },
            {
                "cost_center_name": "Audit",
                "cost_center_shortname": "AU",
            },
            {
                "cost_center_name": "Engineering",
                "cost_center_shortname": "EN",
            },
            {
                "cost_center_name": "Finance & Accountng",
                "cost_center_shortname": "FA",
            },
            {
                "cost_center_name": "Human Resource",
                "cost_center_shortname": "HR",
            },
            {
                "cost_center_name": "Information Technology",
                "cost_center_shortname": "IT",
            },
            {
                "cost_center_name": "Maintenance",
                "cost_center_shortname": "MA",
            },
            {
                "cost_center_name": "Production",
                "cost_center_shortname": "PR",
            },
            {
                "cost_center_name": "Sales",
                "cost_center_shortname": "SA",
            },
            {
                "cost_center_name": "Supply Chain",
                "cost_center_shortname": "AD",
            },
            {
                "cost_center_name": "Other",
                "cost_center_shortname": "OT",
            },
        ]

        for c in costcenter: 
            cc = {
                "id": c['cost_center_name'],
                "cost_center_code": c['cost_center_name'],
                "cost_center_name": c['cost_center_name'],
                "cost_center_shortname": c['cost_center_shortname'],
            }

            CostCenter.objects.create(**cc)















