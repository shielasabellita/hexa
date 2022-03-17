from rest_framework import serializers
from .uom_model import UOM

class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = "__all__"