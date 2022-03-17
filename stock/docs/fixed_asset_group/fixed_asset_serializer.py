from rest_framework import serializers
from .fixed_asset_model import FixedAssetGroup

class FixedAssetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAssetGroup
        fields = "__all__"