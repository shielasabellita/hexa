from rest_framework import serializers
from .location_model import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"