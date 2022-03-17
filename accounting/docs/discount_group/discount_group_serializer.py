from rest_framework import serializers
from .discount_group_model import DiscountGroup

class DiscountGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountGroup
        fields = "__all__"