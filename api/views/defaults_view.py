from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import Company, AccountingPeriod, StatusAndRCode
# serializers
from api.serializers import CompanySerializer, AccountingPeriodSerializer, StatusAndReasonCodeSerializer
# other plugins
# import pandas as pd


class SetupDefaultsView(APIView):

    def get(self, request, format=None):
        coa = self.sync_chart_of_accounts()
        return Response(coa)

    def post(self, request, format=None):
        data = request.data

        validated = self.validate_company(data['company']['company_code'])
        
        if not validated:

            company_serializer = CompanySerializer(data=data['company'])
            acctng_period_serializer = AccountingPeriodSerializer(data=data['accounting_period'])

            if acctng_period_serializer.is_valid() and company_serializer.is_valid():
                acctng_period_serializer.save()
                company_serializer.save()

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

    # def sync_chart_of_accounts(self, company_code=None):
    #     df = pd.read_csv('sample.csv').to_dict('records')
        