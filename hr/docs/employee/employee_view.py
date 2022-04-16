from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document

# model
from .employee_model import Employee

# serializer
from .employee_serializer import EmployeeSerializer

# other packages
import json


class EmployeeView(Document):

    def __init__(self, *args, **kwargs):
        args = (Employee, EmployeeSerializer)
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
            employment_type = ["Direct Hire", "Agency", "Job Order", "On Call"]
            if not data.get("employment_type") in employment_type:
                raise Exception("Employment Type must be in Direct Hire, Agency, Job Order, On Call")

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
        for id in ids: 
            try:
                self.remove(id, request.user)
            except Exception as e:
                return Response("Error on ID {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)



       