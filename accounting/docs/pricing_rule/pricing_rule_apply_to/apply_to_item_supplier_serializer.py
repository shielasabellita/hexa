from rest_framework import serializers
from .apply_to_item_supplier_model import ApplyTo

class ApplyToSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyTo
        fields = "__all__"