from rest_framework import serializers
from .discount_rate_model import DiscountRate

class DiscountRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountRate
        fields = "__all__"