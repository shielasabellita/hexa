from datetime import datetime
from stock.models import Item

def validate_date_and_request_date(trans_date, date_expected):
    date = datetime.strptime(trans_date, "%Y-%m-%d").date()
    date_exp = datetime.strptime(date_expected, "%Y-%m-%d").date()

    if date > date_exp:
        raise Exception("Date Expected must not be before Transaction Date ")


def set_item_details(item):
    item = Item.objects.get(id=item)
    return {
        "id": item.id,
        "item_name": item.item_name,
        "code": item.code,
        "item_shortname": item.item_shortname
    }
    