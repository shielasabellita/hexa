from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api import serializers
# models
from api.models import Company, AccountingPeriod, StatusAndRCode
from api.models.setup_model import ChartOfAccounts

# serializers
from api.serializers.accounting import CompanySerializer


class CompanyView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    model = Company
    

    def get(self, request, company_code, *args, **kwargs):
        try:
            company_inst = Company.objects.get(company_code=company_code)
            company_data = self.serializer_class(company_inst).data
            return Response(company_data,  status=status.HTTP_200_OK)
        except:
            return Response("Company Not Found", status=status.HTTP_404_NOT_FOUND)