from rest_framework import serializers
from .item_price_model import ItemPrice

class ItemPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPrice
        fields = "__all__"