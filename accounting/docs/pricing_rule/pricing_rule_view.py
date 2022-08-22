from shutil import ExecError
from accounting.docs.pricing_rule.pricing_rule_apply_to.apply_to_item_supplier_view import ApplyToView
from rest_framework import status
from rest_framework.response import Response
from setup.core.doc import Document

from .pricing_rule_serializer import PricingRule, PricingRuleSerializer
from .pricing_rule_apply_to.apply_to_item_supplier_serializer import ApplyTo, ApplyToSerializer


import json

class PricingRuleView(Document):

    def __init__(self, *args, **kwargs):
        args = (PricingRule, PricingRuleSerializer)
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
            if self.validate_discount_amt_prcntge(data):
                doc = self.create(data, user=str(request.user))
                if data.get("apply_to"):
                    applyto = data.get("apply_to")
                    for i in applyto['lists']:
                        obj = {
                            applyto['apply_to'].lower(): i,
                            "pricing_rule": doc['id']
                        }
                        apply_to_doc = ApplyToView(ApplyTo, ApplyToSerializer)
                        apply_to_doc.create(data=obj, user=str(request.user))

            return Response(doc)
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


    def validate_discount_amt_prcntge(self, data):
        if data.get("discount_percentage") > 0 and data.get("discount_amt") > 0:
            raise Exception("Discount must be in percentage or amount")
        else:
            return True
