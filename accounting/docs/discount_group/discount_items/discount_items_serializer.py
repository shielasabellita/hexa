from rest_framework import serializers
from .discount_items_model import DiscountItems

class DiscountItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountItems
        fields = "__all__"