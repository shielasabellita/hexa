from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document

# model
from .accounting_period_model import AccountingPeriod

# serializer
from .accounting_period_serializer import AccountingPeriodSerializer

# other packages
import json


class AccountingPeriodView(Document):

    def __init__(self, *args, **kwargs):
        args = (AccountingPeriod, AccountingPeriodSerializer)
        super().__init__(*args,**kwargs)

    # API - GET
    def get(self, request, *args, **kwargs):
        try:
            if request.GET.get('filters', None):
                data = self.get_list(filters=json.loads(request.GET.get('filters', None)))
            else:
                id = request.GET.get('id', None)
                data = self.get_list(id)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - POST
    def post(self, request, *args, **kwargs):
        data = request.data 
        try:
            data = self.create(data, user=str(request.user))
            return Response(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - PUT
    def put(self, request, *args, **kwargs):
        data = request.data 
        try:
            data = self.update(id=data.get("id"), data=data, user=str(request.user))
            return Response(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # API - DELETE
    def delete(self, request, *args, **kwargs):
        ids = request.data['ids']

        not_found_ids = ""
        success = ""
        for id in ids: 
            try:
                self.remove(id, request.user)
                success += "{}, ".format(id)
            except Exception as e:
                not_found_ids += "{}, ".format(id)
        
        return Response("Successfully deleted: {} | Not Found: {}".format(success, not_found_ids), status=status.HTTP_200_OK)



       