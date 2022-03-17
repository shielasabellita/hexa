from rest_framework import serializers
from api.models.hr import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = "__all__"