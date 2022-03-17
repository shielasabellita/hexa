from rest_framework import serializers
from .price_list_model import PriceList

class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = "__all__"