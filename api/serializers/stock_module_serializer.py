from typing import ChainMap
from rest_framework import serializers
from api.models import ItemCategory, ItemCatBrand, ItemCatDepartment, ItemCatForm, ItemCatManufacturer, ItemCatSection, ItemCatSize

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