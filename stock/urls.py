from django.urls import path, include
from .docs.fixed_asset_group.fixed_asset_view import FixedAssetGroupView
from .docs.item_group.item_group_view import ItemGroupView
from .docs.uom.uom_view import UOMView
from .docs.item.item_view import ItemView
from .docs.item.item_price.item_price_view import ItemPriceView
from .docs.item.uom_conversion_detail.uom_conversion_detail_view import UOMConversionDetailView
from .docs.item.supplier_item.supplier_item_view import SupplierItemView


urlpatterns = [
    # MD
    path("docs/fixed_asset", FixedAssetGroupView.as_view(), name='fixed_asset'),
    path("docs/item_group", ItemGroupView.as_view(), name='item_group'),
    path("docs/uom", UOMView.as_view(), name='uom'),
    path("docs/item", ItemView.as_view(), name='item'),
    path("docs/item/item_price", ItemPriceView.as_view(), name='item_price'),
    path("docs/item/item_supplier", SupplierItemView.as_view(), name='item_supplier'),
    path("docs/item/uom_conversion_detail", UOMConversionDetailView.as_view(), name='uom_conversion_detail'),
]
