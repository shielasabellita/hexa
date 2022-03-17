from rest_framework import serializers
from .cost_center_model import CostCenter

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = "__all__"