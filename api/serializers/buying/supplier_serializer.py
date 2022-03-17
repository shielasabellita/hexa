from rest_framework import serializers
from api.models.buying.supplier_model import Supplier, SupplierDiscounts
from api.serializers.accounting import DiscountGroupSerializer

class SupplierSerializer(serializers.ModelSerializer):
    # discount_group1 = DiscountGroupSerializer(read_only=1)
    # discount_group2 = DiscountGroupSerializer(read_only=1)
    # discount_group3 = DiscountGroupSerializer(read_only=1)
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierDiscountsSerializer(serializers.ModelSerializer):
    discount_group = DiscountGroupSerializer(read_only=1)
    class Meta:
        model = SupplierDiscounts
        fields = '__all__'