from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.usermgmt.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # print("Inside the Create Function")
        user = User.objects.create_complete_user(validated_data['username'],
                                                 validated_data['email'],
                                                 validated_data['phone'],
                                                 validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs, ):
        user = authenticate(
            email=attrs['email'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('invalid credentials provided')
        self.instance = user
        return user
