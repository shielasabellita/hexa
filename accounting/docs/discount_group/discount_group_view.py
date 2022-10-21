from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from accounting.docs.discount_group.discount_items.discount_items_view import DiscountItemsView, DiscountItemsSerializer, DiscountItems
from accounting.docs.discount_group.discount_rate_model.discount_rate_model import DiscountRate
from accounting.docs.discount_group.discount_rate_model.discount_rate_serializer import DiscountRateSerializer
from accounting.docs.discount_group.discount_rate_model.discount_rate_view import DiscountRateView
from setup.core.doc import Document

# serializer
from .discount_group_serializer import DiscountGroupSerializer, DiscountGroup

# other packages
import json


class DiscountGroupView(Document):
    dc_rate_doc = DiscountRateView(DiscountRate, DiscountRateSerializer)
    dc_items_doc = DiscountItemsView(DiscountItems, DiscountItemsSerializer)

    def __init__(self, *args, **kwargs):
        args = (DiscountGroup, DiscountGroupSerializer)
        super().__init__(*args,**kwargs)


    # API - GET
    def get(self, request, *args, **kwargs):
        try:
            if request.GET.get('filters', None):
                data = self.get_list(filters=json.loads(request.GET.get('filters', None)))
                for d in data:
                    d.update(self.get_child_data(d['id']))
            else:
                id = request.GET.get('id', None)
                data = self.get_list(id)
                for d in data:
                    d.update(self.get_child_data(d['id']))

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_child_data(self, parent):
        obj = {
            "discounts": self.dc_rate_doc.get_list(filters={"disc_group": parent}),
            "items": self.dc_items_doc.get_list(filters={"disc_group": parent})
        }
        return obj

    # API - POST
    def post(self, request, *args, **kwargs):
        data = request.data 
        try:
            total = 0
            if not data.get("discounts"):
                return Response("Please input discount rates", status=HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                for i in data.get("discounts"):
                    total += i['disc_rate']
            
            obj = {
                "discount_name": data['discount_name'],
                "total_discount": total
            }

            if data.get('code'):
                obj.update({'code': data.get('code')})
            
            parent_doc = self.create(obj, user=str(request.user))
            rate_dt = []
            items_dt = []
            for i in data.get('discounts'):
                i.update({
                    "disc_group": parent_doc.get("id")
                })
                rate_dt.append(self.dc_rate_doc.create(i, user=str(request.user)))

            
            # items
            if data.get("items"):
                for i in data.get('items'):
                    i.update({
                        "disc_group": parent_doc.get("id")
                    })
                    items_dt.append(self.dc_items_doc.create(data=i, user=str(request.user)))

            dt = parent_doc
            dt.update({
                "discounts": rate_dt,
                "items": items_dt
            })
            return Response(dt)
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


