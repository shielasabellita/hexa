from rest_framework import serializers
from .parent_company_model import ParentCompany

class ParentCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCompany
        fields = "__all__"