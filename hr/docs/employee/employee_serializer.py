from rest_framework import serializers
from .employee_model import VatGroup

class VatGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatGroup
        fields = "__all__"