from os import stat
from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api import serializers
# models
from api.models.settings_model import ChartOfAccounts

# serializers
from api.serializers.accounting import ChartOfAccountsSerializer, ChartOfAccountsSerializer


class ChartOfAccountsView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    serializer_class = ChartOfAccountsSerializer
    model = ChartOfAccounts
    

    def get(self, request, company_code, *args, **kwargs):
        try:
            company_inst = ChartOfAccounts.objects.filter(company_id=company_code)
            data = self.serializer_class(company_inst, many=True).data

            return Response(data,  status=status.HTTP_200_OK)
        except:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)