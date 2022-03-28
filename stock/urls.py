from django.urls import path, include
from .docs.fixed_asset_group.fixed_asset_view import FixedAssetGroupView
from .docs.item_group.item_group_view import ItemGroupView
from .docs.uom.uom_view import UOMView
from .docs.item.item_view import ItemView


urlpatterns = [
    # MD
    path("docs/fixed_asset", FixedAssetGroupView.as_view(), name='fixed_asset'),
    path("docs/item_group", ItemGroupView.as_view(), name='item_group'),
    path("docs/uom", UOMView.as_view(), name='uom'),
    path("docs/item", ItemView.as_view(), name='item'),
]
