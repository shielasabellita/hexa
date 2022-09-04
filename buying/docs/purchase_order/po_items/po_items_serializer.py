from rest_framework import serializers
from .po_items_model import POItems

class POItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = POItems
        fields = "__all__"