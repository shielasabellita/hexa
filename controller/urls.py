from django.urls import path, include


# api
from controller.controllers.item import get_item_rate, get_supplier_discount

urlpatterns = [
    # api
    path("item/get_item_rate", get_item_rate, name='get_rate'),
    path("po/get_supplier_discount/<supplier>", get_supplier_discount, name='get_supplier_discount'),
]