from rest_framework import serializers
from .supplier_group_model import SupplierGroup

class SupplierGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierGroup
        fields = "__all__"