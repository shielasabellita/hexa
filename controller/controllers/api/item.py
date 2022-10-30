from rest_framework.decorators import api_view
from rest_framework.response import Response
import decimal
from controller.controllers.item import _get_item_rate, _get_supplier_discount


@api_view(['GET', 'POST'])
def get_item_rate(request):
    """
        args: {
            "price_list": "df94b235c7ce44d7a7ef0737c6762338",
            "item": "f7ddfbcc117843639aff3c29c827a2d3",
            "uom": "824b1874e1cd4ff98a98a9c3419404d3", 
            "supplier": "5d3d88f63dfd44d9818225fc66006ebc",
            "rate": 10, // rate can be get from item price master
            "qty": 3
        }
    """
    data = request.data
    res = _get_item_rate(data)
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