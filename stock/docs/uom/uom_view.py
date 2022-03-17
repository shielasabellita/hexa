from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from setup.core.doc import Document

# model
from .uom_model import UOM

# serializer
from .uom_serializer import UOMSerializer

# other packages
import json


class UOMView(Document):

    def __init__(self, *args, **kwargs):
        args = (UOM, UOMSerializer)
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
        for id in ids: 
            try:
                self.remove(id, request.user)
            except Exception as e:
                return Response("Error on ID {}: {}".format(id, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)



       