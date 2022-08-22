import decimal
from accounting.docs.discount_group.discount_group_model import DiscountGroup
from buying.docs.supplier.supplier_discounts.supplier_discounts_model import SupplierDiscounts
from buying.docs.supplier.supplier_model import Supplier
from stock.docs.item.supplier_item.supplier_item_model import SupplierItem
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
            "item": "f7ddfbcc117843639aff3c29c827a2d3",
            "uom": "824b1874e1cd4ff98a98a9c3419404d3", 
            "supplier": "5d3d88f63dfd44d9818225fc66006ebc",
            "rate": 10, // rate can be get from item price master
            "qty": 3
        }
    """
    data = request.data

    pl_doc = PriceList.objects.get(id=data['price_list'])
    item_doc = Item.objects.get(id=data['item'])
    vat_percentage = get_percent(int(item_doc.vat_group.rate))

    try:
        item_price = ItemPrice.objects.get(item=item_doc, price_list=pl_doc)
    except:
        item_price = None

    vat = 0
    if item_price: 
        vat = 1 + decimal.Decimal(vat_percentage)
    else:
        vat = 1 + vat_percentage


    rate = 0 if not (item_price.rate if item_price else data.get("rate")) else (item_price.rate if item_price else data.get("rate"))
    amount = get_item_amount(rate, data.get("qty"))

    res = {
        "vat_rate": item_doc.vat_group.rate,
        "vat_group": item_doc.vat_group.vat_group_name,
        "item_id": item_doc.id,
        "code": item_doc.code,
        "item_name": item_doc.item_name,
        "item_shortname": item_doc.item_shortname,
        "rate": rate,
        "gross_rate": flt(rate/vat, 2),
        "amount": amount,
        "qty": data.get("qty"),
        "uom_id": item_doc.base_uom.id,
        "uom": item_doc.base_uom.uom,
    }

    print(get_supplier_discount(data.get("supplier")), data.get("item"))
    
    return Response(res)


def get_item_amount(rate, qty):
    return rate * qty


def generate_item_price_if_zero(item, rate, uom, price_list, supplier):
    ItemPrice.objects.create(**{
        "item": item,

    })

@api_view(['GET', 'POST'])
def get_supplier_discount(request, supplier, item=None):
    """
        gets the tagged supplier discount in item and in supplier master
        lack: pricing rule
    """

    discounts = {
            "is_per_item": 0,
            "discounts": [],
            "total_disc": 0,
            "item": item
        }
    
    sup_item = SupplierItem.objects.filter(item=item, supplier=supplier)
    if sup_item:
        discounts['is_per_item'] = 1
    

    try:
        total_disc = 0
        supplier_doc = Supplier.objects.get(id=supplier)
        disc_group = SupplierDiscounts.objects.filter(supplier=supplier_doc)
        
        for disc in disc_group:
            discounts["discounts"].append({
                "discount_name": disc.discount_group.discount_name,
                "total_disc": disc.discount_group.total_discount
            })

            total_disc += disc.discount_group.total_discount

        discounts.update({
            "total_disc": total_disc,
            "supplier": supplier_doc.id,
            "supplier_name": supplier_doc.sup_name,
        })
        return Response(discounts)
    except:
        return Response(discounts)