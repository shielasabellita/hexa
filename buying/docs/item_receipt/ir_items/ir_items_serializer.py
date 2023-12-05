from rest_framework import serializers
from .ir_items_model import IRItems

class IRItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IRItems
        fields = "__all__"
