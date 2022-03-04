from rest_framework import serializers
from api.models.stock import ItemGroup, FixedAssetGroup
from api.models.defaults_model import PriceList



class ItemSerializerGroup(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = '__all__'


class FixedAssetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAssetGroup
        fields = '__all__'


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'