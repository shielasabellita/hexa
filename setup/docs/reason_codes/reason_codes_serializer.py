from rest_framework import serializers
from .reason_codes_model import StatusAndRCode

class StatusAndRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusAndRCode
        fields = "__all__"