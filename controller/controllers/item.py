import decimal
from accounting.docs.discount_group.discount_group_model import DiscountGroup
from accounting.docs.discount_group.discount_group_serializer import DiscountGroupSerializer
from accounting.docs.discount_group.discount_group_view import DiscountGroupView
from buying.docs.supplier.supplier_discounts.supplier_discounts_model import SupplierDiscounts
from buying.docs.supplier.supplier_model import Supplier
from stock.docs.item.supplier_item.supplier_item_model import SupplierItem
from stock.models import Item, ItemPrice
from accounting.models import PriceList, VatGroup

from controller.utils import get_percent, flt






def _get_item_rate(data):
    pl_doc = PriceList.objects.get(id=data['price_list'])
    item_doc = Item.objects.get(id=data['item'])
    vat_percentage = get_percent(int(item_doc.vat_group.rate))

    try:
        item_price = ItemPrice.objects.get(item=item_doc, price_list=pl_doc)
    except:
        item_price = None

    vat_decimal = 0
    if item_price: 
        vat_decimal = 1 + decimal.Decimal(vat_percentage)
    else:
        vat_decimal = 1 + vat_percentage

    # item rate
    rate = 0
    if data.get("rate") or item_price:
        rate = data.get("rate")
    elif not data.get('rate') and item_price:
        rate = item_price

    rate = decimal.Decimal(rate)
    amount = data.get("qty") * rate

    
    # DISCOUNTING
    total_discount_percentage = 0
    # discount group
    sup_disc = _get_supplier_discount(data.get('supplier'), data.get('item'))
    if sup_disc:
        for sd in sup_disc:
            for i in sd.get('items'):
                itm = dict(i)
                if itm['item'] == data.get('item'):
                    total_discount_percentage += sd['total_discount']

    # pricing rule

    # additional discount
    if data.get("additional_discount"):
        total_discount_percentage += data.get("additional_discount")


    # totals ====================
    gross_rate = rate

    if vat_decimal > 0:
        gross_rate = rate/vat_decimal

    total_discount_rate = decimal.Decimal(decimal.Decimal(total_discount_percentage)/gross_rate)
    
    net_rate = (gross_rate - total_discount_rate) * data.get('qty')
    amount_payable = 0

    vat_rate = 0
    if vat_decimal > 0:
        vat_rate = net_rate * get_percent(decimal.Decimal(item_doc.vat_group.rate))
        amount_payable = net_rate + vat_rate
    

    # Return
    res = {
        "vat_group_id": item_doc.vat_group.id,
        "vat_group_name": item_doc.vat_group.vat_group_name,
        "item_id": item_doc.id,
        "code": item_doc.code,
        "item_name": item_doc.item_name,
        "item_shortname": item_doc.item_shortname,
        "vat_rate": item_doc.vat_group.rate,
        "total_discount_percentage": total_discount_percentage,
        "vat_amount": flt(vat_rate, 2),
        "gross_rate": flt(gross_rate, 2),
        "rate": flt(rate, 2),
        "amount": flt(amount, 2),
        "net_rate": flt(net_rate, 2),
        "amount_payable": flt(amount_payable, 2),
        "qty": data.get("qty"),
        "uom_id": item_doc.base_uom.id,
        "uom_name": item_doc.base_uom.uom,
    }

    return res


# fn
def _get_supplier_discount(supplier, item, pricelist=None):
    """
        gets the tagged supplier discount in item and in supplier master
        optional: pricing rule
    """
    
    try:
        kwargs = {
            "supplier": supplier,
            "item": item
        }
        if pricelist:
            kwargs.update({
                "price_list": pricelist
            })

        # print(kwargs)
        sup_item = SupplierItem.objects.get(**kwargs)
    except:
        sup_item = None


    if sup_item:
        sup_discs = SupplierDiscounts.objects.filter(supplier=supplier)
        discounts = []
        if sup_discs:
            for sd in sup_discs:
                disc_group_doc = DiscountGroupView(DiscountGroup, DiscountGroupSerializer)
                disc_list = disc_group_doc.get_list(id=sd.discount_group.id)
                disc_list.update(disc_group_doc.get_child_data(sd.discount_group.id))
                discounts.append(disc_list)

        return discounts
    else:
        return None



