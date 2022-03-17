from rest_framework import serializers
from .withholding_tax_model import WithHoldingTaxGroup

class WithHoldingTaxGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithHoldingTaxGroup
        fields = "__all__"