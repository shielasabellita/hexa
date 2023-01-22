from django.urls import path, include


# api
from controller.controllers.api.item import get_transaction_details, get_supplier_discount

urlpatterns = [
    # api
    path("item/get_transaction_details", get_transaction_details, name='get_transaction_details'),
    path("po/get_supplier_discount", get_supplier_discount, name='get_supplier_discount'),
]