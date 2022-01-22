from django.db.models.base import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

# models
from api.models.stock import Item

# serializers 
from api.serializers.stock import ItemSerializer
from api.utils.helpers import move_to_deleted_document
from api.utils.naming import set_naming_series

import json

class ItemView(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    
    model = Item
    serializer_class = ItemSerializer
    
    
    def get(self, request, *args, **kwargs): 
        items = self.model.objects.all()
        data = self.serializer_class(items, many=True).data
        
        id = request.GET.get('id', None)
        print(id)

        if id:
            try:
                item = self.model.objects.get(id=id)
                data = self.serializer_class(item).data

                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response("Item not found", status=status.HTTP_404_NOT_FOUND)

        return Response(data, status=status.HTTP_200_OK)



    def post(self, request):
        data = request.data
        
        data.update({
            "id": self.set_name()
        })
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def put(self, request, *args, **kwargs):
        id = request.data['id']

        if id:
            inst = get_object_or_404(self.model.objects.all(), id=id)
            serializer = self.serializer_class(inst, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Please enter ID", status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, *args, **kwargs):
        ids = request.data['ids']
        
        for id in ids: 
            try:
                inst = get_object_or_404(self.model.objects.all(), id=id)
                move_to_deleted_document("Item", id, json.dumps(model_to_dict(inst)), request.user)
                
                inst.delete() 
            except Exception as e:
                return Response("ID {} Not Found".format(id), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Successfully deleted", status=status.HTTP_200_OK)


    def set_name(self):
        return set_naming_series("ITM")
    

