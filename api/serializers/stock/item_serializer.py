from rest_framework import serializers
from api.models.stock import Item
# from api.serializers import UOMSerializer, VatGroupSerializer, ChartOfAccountsSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
