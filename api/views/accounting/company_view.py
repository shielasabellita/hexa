from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# models
from api.models import Company, AccountingPeriod, StatusAndRCode, ParentCompany
from api.models.setup_model import ChartOfAccounts

# serializers
from api.utils.helpers import move_to_deleted_document
from django.forms.models import model_to_dict
from api.serializers.accounting import CompanySerializer, ParentCompanySerializer

import json


class CompanyView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    model = Company
    

    def get(self, request, *args, **kwargs):
        try:
            company_code = request.GET.get('id', None)
            company_inst = Company.objects.get(company_code=company_code)
            company_data = self.serializer_class(company_inst).data
            return Response(company_data,  status=status.HTTP_200_OK)
        except:
            return Response("Company Not Found", status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def put(self, request):
        try:
            company_code = request.GET.get('id', None)
            inst = Company.objects.get(company_code=company_code)
            serializer = self.serializer_class(inst, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response(str(e))


    def delete(self, request):
        ids = request.data['ids']
        for id in ids:
            try:
                inst = Company.objects.get(company_code=id)
                move_to_deleted_document("Company", id, model_to_dict(inst), request.user)
                inst.delete()
                return Response("Successfully deleted", status=status.HTTP_200_OK)
            except Exception as e:
                return Response("Error on ID {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
       

class ParentCompanyView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    serializer_class = ParentCompanySerializer
    model = ParentCompany

    def get(self, request):
        id = request.GET.get('id', None)
        try:
            inst = self.model.objects.get(id=id)
            serializer = self.serializer_class(inst).data
            return Response(serializer,  status=status.HTTP_200_OK)
        except:
            return Response("Parent Company Not Found", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    # def put(self, request):
    #     try:
    #         id = request.data['id']
    #         inst = self.model.objects.get(id=id)
    #         inst.id = request.data['new_id']
    #         inst.save()
    #         # serializer = self.serializer_class(inst, data=request.data)
    #         # if serializer.is_valid():
    #         #     serializer.save()
    #         #     return Response(serializer.data)
    #         # else:
    #         #     return Response(serializer.errors)
    #     except Exception as e:
    #         return Response(str(e))


    def delete(self, request):
        ids = request.data['ids']
        
        for id in ids:
            try:
                inst = self.model.objects.get(id=id)
                move_to_deleted_document("Parent Company", id, model_to_dict(inst), request.user)
                inst.delete()
                return Response("Successfully deleted", status=status.HTTP_200_OK)
            except Exception as e:
                return Response("Error on ID {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)