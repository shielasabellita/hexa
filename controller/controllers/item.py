import decimal
from stock.models import Item, ItemPrice
from accounting.models import PriceList, VatGroup

from controller.utils import get_percent, flt

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def get_item_rate(request):
    """
        args: {
            "price_list": "df94b235c7ce44d7a7ef0737c6762338",
            "item": "fddefa5e0cfa4b5fa59ba865df9dfa74",
            "uom": "824b1874e1cd4ff98a98a9c3419404d3", 
            "supplier": "5d3d88f63dfd44d9818225fc66006ebc",
            "rate": 1 // not required
        }

    """
    data = request.data

    pl_doc = PriceList.objects.get(id=data['price_list'])
    item_doc = Item.objects.get(id=data['item'])
    vat_percentage = get_percent(int(item_doc.vat_group.rate))

    rate = 0
    try:
        item_price = ItemPrice.objects.get(item=item_doc, price_list=pl_doc)
    except:
        item_price = None

    vat = 0
    if item_price: 
        vat = 1 + decimal.Decimal(vat_percentage)
    else:
        vat = 1 + vat_percentage

    rate = (item_price.rate if item_price else data.get("rate")) * vat
    
    res = {
        "vat_rate": item_doc.vat_group.rate,
        "item": item_doc.id,
        "rate": flt(rate, 2)
    }
    return Response(res)


def get_item_amount(rate, qty):
    return rate * qty


