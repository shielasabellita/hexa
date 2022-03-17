from pyexpat import model
from rest_framework import serializers
from api.models.setup_model import Branch, Location
from api.serializers.accounting import CompanySerializer


class Branch(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Branch
        field = '__all__'


class Location(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Location
        field = '__all__'