from rest_framework import status
from setup.docs.user.auth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from setup.models import *

# other packages
import json, traceback
from setup.docs.utils.naming import set_naming_series, generate_id
from setup.docs.utils.helpers import move_to_deleted_document
from django.forms.models import model_to_dict


class Document(APIView):
    authentication_classes = (CustomAuthentication, )
    permission_classes = [IsAuthenticated]

    serializer_class = ""
    model = ""

    def __init__(self, *args, **kwargs):
        if args:
            self.model = args[0]
            self.serializer_class = args[1]


    def get_list(self, id=None, filters=None, fk_fields=None, models_serializer=None):
        """
            no id if get_all , set filters if get by filters
        """
        
        inst = self.model.objects.all().order_by("-updated_at")
        serializer = self.serializer_class(inst, many=True)

        if id != None:
            inst = self.model.objects.get(id=id)
            serializer = self.serializer_class(inst)
        elif filters:
            inst = self.model.objects.filter(**filters)
            serializer = self.serializer_class(inst, many=True)
        
        data = serializer.data
        if fk_fields and models_serializer:
            data = self.get_linked_data(serializer.data, fk_fields, models_serializer)
        return data
    
    def get_linked_data(self, data=None, fk_fields=None, models_serializer=None):
        dt = data
        if isinstance(dt, list):
            for d in dt:
                for i in fk_fields:
                    if d[i]:
                        inst = models_serializer[i][0].objects.get(id=d[i])
                        serializer = models_serializer[i][1](inst).data
                        d.update({
                            i: self.pop_default_fields(serializer)
                        })
        else:
            for i in fk_fields:
                if dt[i]:
                    inst = models_serializer[i][0].objects.get(id=dt[i])
                    serializer = models_serializer[i][1](inst).data
                    dt.update({
                        i: self.pop_default_fields(serializer)
                    })

        return dt
    
    def pop_default_fields(self, serializer):
        serializer.pop("created_by")
        serializer.pop("created_at")
        serializer.pop("updated_by")
        serializer.pop("updated_at")
        return serializer

    
    def sql(self, query):
        return self.model.objects.raw(query)


    def create(self, data, user='Guest'):
        if data.get("code"):
            code = set_naming_series(data['code'])
        else:
            default = self.model._meta.get_field("code").default
            code = set_naming_series(default)
        
        data.update({
            "id": generate_id(),
            "code": code,
            "created_by": user,
            "updated_by": user,
        })
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            raise Exception("Error: {}".format(serializer.errors))


    def update(self, id, data, user='Guest'):
        data.update({
            "updated_by": user
        })

        inst = self.model.objects.get(id=id)
        serializer = self.serializer_class(inst, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            raise Exception(serializer.errors)


    def remove(self, id, table_name='None', user='Guest'):
        inst = self.model.objects.get(id=id)
        move_to_deleted_document(table_name, id, model_to_dict(inst), user)
        inst.delete()
        return Response("Successfully deleted", status=status.HTTP_200_OK)
       


       