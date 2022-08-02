from django.urls import path, include


# api
from controller.controllers.item import get_item_rate

urlpatterns = [
    # api
    path("item/get_item_rate", get_item_rate, name='get_rate'),
]