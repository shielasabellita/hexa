from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from setup.models import Company, AccountingPeriod
from accounting.models import ChartOfAccounts, CostCenter, PriceList, StatusAndRCode, SupplierGroup, VatGroup, WithHoldingTaxGroup
from stock.docs.uom.uom_model import UOM
from stock.docs.item_group.item_group_model import ItemGroup
from stock.docs.fixed_asset_group.fixed_asset_model import FixedAssetGroup
from setup.docs.company.company_serializer import CompanySerializer


from setup.core.doc import Document
from setup.docs.utils.naming import set_naming_series, generate_id
from setup.docs.utils.helpers import get_coa_csv_path, get_rcs_csv_path

# other plugins
import pandas as pd


class SetupDefaultsView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        company_doc = Document(Company, CompanySerializer)
        if_company_exist = company_doc.get_list(filters={
                            "company_name": data['company'].get("company_name"), 
                            "company_shortname": data['company'].get("company_shortname")
                        })
        if if_company_exist:
            return Response("Database already used", status=status.HTTP_403_FORBIDDEN)
        else: 
            ## set company series code
            company_code = set_naming_series('COMP_{5}')
            data['company'].update({
                "id": generate_id(),
                "code": company_code
            })
            company_inst = Company.objects.create(**data['company'])
            company_inst.save()

            ## set accounting period code
            acc_period_code = set_naming_series("ACC-PRD_{5}")
            data['accounting_period'].update({
                    "id": generate_id(),
                    "code": acc_period_code
                })

            AccountingPeriod.objects.create(**data['accounting_period'], company=company_inst)
            
            self.sync_coa(company_inst) # account
            self.sync_reason_codes() # account
            self.sync_vatgroup() # account
            self.sync_fixed_asset_group()  # stock
            self.sync_itemgroup()  # stock 
            self.sync_uom()  # stock
            self.sync_price_list() # account
            self.sync_supplier_group() # account
            self.sync_costcenter() # account

            return Response(CompanySerializer(company_inst).data, status=status.HTTP_200_OK)            

    def sync_coa(self, company):
        coas = pd.read_csv(get_coa_csv_path()).to_dict('records')
        for coa in coas:

            coa.update({
                "id": generate_id(),
                "code": set_naming_series("COA_{9}")
            })

            ChartOfAccounts.objects.create(**coa)



    def sync_reason_codes(self):
        rcs = pd.read_csv(get_rcs_csv_path(), keep_default_na=False).to_dict('records')
        for rc in rcs:
            rc.update({
                "id": generate_id(),
                "code": set_naming_series("RC_{9}")
            })
            StatusAndRCode.objects.create(**rc)



    def sync_vatgroup(self):
        vat = [
                {
                    "vat_group_name": "VAT-Exempt",
                    "rate": 0
                }, 
                {
                    "vat_group_name": "Zero Rated",
                    "rate": 0
                }, 
                {
                    "vat_group_name": "Input Tax",
                    "rate": 12
                }, 
                {
                    "vat_group_name": "Output Tax",
                    "rate": 12
                }
            ]
        for v in vat: 
            v.update({
                "id": generate_id(),
                "code": set_naming_series("VAT_{5}")
            })
            VatGroup.objects.create(**v)

    

    def sync_itemgroup(self):
        item_groups = ["Product", "Asset", "Material", "Service", "Other"]
        for ig in item_groups:
            itm = {
                "id": generate_id(),
                "code": set_naming_series("ITM-GRP_{5}"),
                "item_group_name": ig
            }
            ItemGroup.objects.create(**itm)


    
    def sync_fixed_asset_group(self):
        fas = ["Motor Vehicle", "Office Equipment", "Furniture and Fixture"]
        for fa in fas:
            fassts = {
                "id": generate_id(),
                "code": set_naming_series("FXD-ASS_{5}"),
                "fixed_asset_name": fa
            }
            FixedAssetGroup.objects.create(**fassts)


    def sync_uom(self):
        uoms = [
            {
                "uom": "Unit"
            },
            {
                "uom": "Case"
            },
        ]
        for uom in uoms: 
            uom.update({
                "id": generate_id(),
                "code": set_naming_series("UOM_{5}")
            })
            UOM.objects.create(**uom)



    def sync_price_list(self):
        prices = [
            {
                "price_list_name": "Buying",
                "is_buying": 1,
                "is_selling": 0,
                "is_transfer": 0,
            },
            {
                "price_list_name": "Selling",
                "is_buying": 0,
                "is_selling": 1,
                "is_transfer": 0,
            },
            {
                "price_list_name": "Transfer",
                "is_buying": 0,
                "is_selling": 0,
                "is_transfer": 1,
            },
        ]

        for p in prices: 
            p.update({
                "id": generate_id(),
                "code": set_naming_series("PR-LST_{5}")
            })
            PriceList.objects.create(**p)   



    def sync_supplier_group(self):
        groups = ["Local", "Service", "Concessionaire", "Intercompany", "Imported"]
        
        for g in groups:
            sg = {
                "id": generate_id(),
                "code": set_naming_series("SUP-GRP_{5}"),
                "supplier_group": g
            }
            SupplierGroup.objects.create(**sg)


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
                "id": generate_id(),
                "code": set_naming_series("CST-CNTR_{5}"),
                "cost_center_name": c['cost_center_name'],
                "cost_center_shortname": c['cost_center_shortname'],
            }

            CostCenter.objects.create(**cc)

