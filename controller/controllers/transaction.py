from accounting.models import PriceList
from stock.models import FixedAssetGroup, ItemGroup


def validate_price_list(price_list, type='Purchasing'):
    if isinstance(price_list, str):
        price_list = PriceList.objects.get(id=price_list)

    if type == 'Purchasing':
        if (price_list.is_buying == 1 and price_list.is_selling == 0) or (price_list.is_buying == 1 and price_list.is_selling == 1):
            return price_list
        else:
            raise Exception("Price list must be a Purchasing type")

    elif type == 'Selling':
        if (price_list.is_buying == 0 and price_list.is_selling == 1) or (price_list.is_buying == 1 and price_list.is_selling == 1):
            return price_list
        else:
            raise Exception("Price list must be a Selling type")

    elif type == 'Transfer':
        if (price_list.is_transfer == 1):
            return price_list
        else:
            raise Exception("Price list must be a Transfer type")


def validate_item_group(item_group, fixed_asset=None):
    item_group = ItemGroup.objects.get(id=item_group)
    if item_group.item_group_name == 'Asset':
        if not fixed_asset:
            raise Exception ("Please specify Fixed Asset Group")
        else:
            fixed_asset_group = FixedAssetGroup.objects.get(id=fixed_asset)
            return [item_group, fixed_asset_group]
    
    return [item_group]


