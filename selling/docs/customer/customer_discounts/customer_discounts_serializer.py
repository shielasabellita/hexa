from rest_framework import serializers
from .customer_discounts_model import CustomerDiscounts

class CustomerDiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDiscounts
        fields = "__all__"