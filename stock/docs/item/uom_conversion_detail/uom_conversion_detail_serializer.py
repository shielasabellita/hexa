from rest_framework import serializers
from .vat_group_model import VatGroup

class VatGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatGroup
        fields = "__all__"