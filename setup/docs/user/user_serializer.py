from rest_framework import serializers


from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'



    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

