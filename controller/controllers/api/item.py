from rest_framework.decorators import api_view
from rest_framework.response import Response
import decimal
from controller.controllers.item import _get_transaction_details, _get_supplier_discount


@api_view(['GET', 'POST'])
def get_transaction_details(request):
    data = request.data
    res = _get_transaction_details(data)
    return Response(res)



@api_view(['GET'])
def get_supplier_discount(request):
    data = request.GET
    res = _get_supplier_discount(data.get('supplier'), data.get('item'))

    if data.get('pricelist', None):
        res = _get_supplier_discount(data.get('supplier'), data.get('item'), data.get('pricelist'))

    if res:
        return Response(res)
    else:
        raise Exception("No Suppliers found in Item")