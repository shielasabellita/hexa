from os import stat
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import Company, AccountingPeriod, StatusAndRCode

# serializers
from api.serializers import CompanySerializer, AccountingPeriodSerializer, StatusAndReasonCodeSerializer
from api.serializers.defaults_serializer import ChartOfAccountsSerializer

# other plugins
import pandas as pd

# helpers
from api.utils.helpers import get_static_path, get_coa_csv_path


class SetupDefaultsView(APIView):

    def get(self, request, company_code=None, format=None):
        # print(request.GET)
        settings = self.get_default_settings(company_code)
        print(settings)
        settings_data = []
        settings_data.append(CompanySerializer(settings[0]).data)
        # settings_data.append(AccountingPeriodSerializer(settings[1]).data)
        # settings_data.append(ChartOfAccountsSerializer(settings[2]).data)
        
        if settings_data:
            return Response(settings_data, status.HTTP_200_OK)
        else:
            return Response("Not Found", status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        data = request.data

        data['accounting_period'].update({
            "id": "{} - {}".format(data['accounting_period']['acctng_period_code'], data['company']['company_code'])
        })

        validated = self.validate_company(data['company']['company_code'])
        
        if not validated:

            company_serializer = CompanySerializer(data=data['company'])
            acctng_period_serializer = AccountingPeriodSerializer(data=data['accounting_period'])
            
            if acctng_period_serializer.is_valid() and company_serializer.is_valid():
                acctng_period_serializer.save()
                company_serializer.save()
                self.sync_chart_of_accounts(company_code=data['company']['company_code'])

                setup_data = {}
                setup_data.update({"company": company_serializer.data})
                setup_data.update({"accounting_period": acctng_period_serializer.data})

                return Response(setup_data, status=status.HTTP_201_CREATED)
            else:
                errors = {}
                errors.update(acctng_period_serializer.errors)
                errors.update(company_serializer.errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Company {} already exist".format(data['company']['company_code']), status=status.HTTP_403_FORBIDDEN)

    def validate_company(self, company_code):
        try:
            if Company.objects.get(company_code=company_code):
                return True
        except:
            return False

    def sync_chart_of_accounts(self, company_code):
        coas = pd.read_csv(get_coa_csv_path()).to_dict('records')
        
        updated_coas = []
        for coa in coas:
            coa.update({
                "id": "{} - {} - {}".format(coa['account_code'], coa['account_name'], company_code),
                "company_id": company_code
            })
            updated_coas.append(coa)

        for updated_coa in updated_coas:
            coa_serializer = ChartOfAccountsSerializer(data=updated_coa)
            if coa_serializer.is_valid():
                print('serialized data',coa_serializer.data)
            else:
                return Response(coa_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return True

    def get_default_settings(self, company_code):
        company = Company.objects.get(company_code=company_code)
        accounting_period = AccountingPeriod.objects.all()
        coa = AccountingPeriod.objects.all()

        return [company, accounting_period, coa]
