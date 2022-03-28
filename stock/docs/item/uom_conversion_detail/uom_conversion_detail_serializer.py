from rest_framework import serializers
from .uom_conversion_detail_model import UOMConversionDetail

class UOMConversionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOMConversionDetail
        fields = "__all__"