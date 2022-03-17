from typing import ChainMap
from rest_framework import serializers
from api.models import ItemCategory, ItemCatBrand, ItemCatDepartment, ItemCatForm, ItemCatManufacturer, ItemCatSection, ItemCatSize, UOM
from api.models.buying.supplier_model import SupplierItems, ItemPrice
from api.models.stock.item_model import UOMConversionDetail
from api.serializers.buying.supplier_serializer import SupplierSerializer


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'


class ItemCatBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCatBrand
        fields = '__all__'


class ItemCatDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCatDepartment
        fields = '__all__'


class ItemCatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCatForm
        fields = '__all__'


class ItemCatManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCatManufacturer
        fields = '__all__'


class ItemCatSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCatSection
        fields = '__all__'


class ItemCatSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCatSize
        fields = '__all__'


class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'


class SupplierItemsSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    class Meta:
        model = SupplierItems
        fields = '__all__'


class ItemPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPrice
        fields = '__all__'


class UOMConversionFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOMConversionDetail
        fields = "__all__"