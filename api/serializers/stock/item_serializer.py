from rest_framework import serializers
from api.models.stock import Item



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
