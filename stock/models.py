from django.db import models
from stock.docs.uom.uom_model import UOM
from stock.docs.item_group.item_group_model import ItemGroup
from stock.docs.fixed_asset_group.fixed_asset_model import FixedAssetGroup
from stock.docs.item.item_model import Item
from stock.docs.item.item_price.item_price_model import ItemPrice
from stock.docs.item.supplier_item.supplier_item_model import SupplierItem
from stock.docs.item.uom_conversion_detail.uom_conversion_detail_model import UOMConversionDetail
from stock.docs.categorization.categorization_model import *



# uom
UOM()

# item
Item()

# item group
ItemGroup()

# fixed asset group
FixedAssetGroup()

# item -> item price
ItemPrice()

# item -> supplier item
SupplierItem()

# item -> uom conversion detail
UOMConversionDetail()

ItemCatBrand()
ItemCatDepartment()
ItemCategory()
ItemCatForm()
ItemCatManufacturer()
ItemCatSection()
ItemCatSize()