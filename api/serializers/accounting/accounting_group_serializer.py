from typing import ChainMap
from rest_framework import serializers
from api.models import VatGroup, DiscountGroup, SupplierGroup, WithHoldingTaxGroup, Branch, Location


class VatGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatGroup
        fields = '__all__'


class DiscountGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountGroup
        fields = '__all__'


class SupplierGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierGroup
        fields = '__all__'


class WithHoldingTaxGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithHoldingTaxGroup
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
