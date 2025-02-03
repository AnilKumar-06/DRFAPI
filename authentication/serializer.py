from . models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.core.exceptions import ValidationError


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=5)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
        
    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise ValidationError("User with username already exists")
        
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("User with email already exists")
        
        phone_number_exists = User.objects.filter(phone_number = attrs['phone_number']).exists()
        if phone_number_exists:
            raise ValidationError("User with phone number already exists")
        
        return super().validate(attrs)