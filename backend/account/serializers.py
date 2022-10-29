from dataclasses import field, fields
from pyexpat import model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Application,slot
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

    
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        

        return token
    

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password','id','is_active']
        extra_kwargs={
            'password':{'write_only':True},
            
        }
    def create(self, validated_data):
        pwd = validated_data.pop("password")
        instance=self.Meta.model(**validated_data)
        instance.set_password(pwd)
        instance.save()
        return instance

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields='__all__'

class slotSerializer(serializers.ModelSerializer):

     class Meta:
        model=slot
        fields='__all__'