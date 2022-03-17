from rest_framework import serializers
from .item_group_model import ItemGroup

class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = "__all__"