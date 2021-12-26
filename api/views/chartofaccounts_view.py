from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api import serializers
# models
from api.models import Company, AccountingPeriod, ChartOfAccounts

# serializers
from api.serializers import ChartOfAccountsSerializer, ChartOfAccountsSerializer


class ChartOfAccountsView(APIView):
    serializer_class = ChartOfAccountsSerializer
    model = ChartOfAccounts
    

    def get(self, request, company_code, *args, **kwargs):
        try:
            company_inst = ChartOfAccounts.objects.filter(company_id=company_code)
            data = []
            for inst in company_inst:
                data.append(self.serializer_class(inst).data)

            return Response(data,  status=status.HTTP_200_OK)
        except:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)