from rest_framework import serializers
from .supplier_item_model import SupplierItem

class SupplierItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierItem
        fields = "__all__"