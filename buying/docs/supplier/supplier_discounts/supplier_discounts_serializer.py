from rest_framework import serializers
from .supplier_discounts_model import SupplierDiscounts

class SupplierDiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierDiscounts
        fields = "__all__"