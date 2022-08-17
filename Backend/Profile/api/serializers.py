from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Profile.models import *

User = get_user_model()


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']
        read_only_fields = []


class UserViewFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'first_name', 'last_name', 'email']
        read_only_fields = []


class ProfileSerializer(serializers.ModelSerializer):
    user = UserViewFullSerializer(many=False)

    class Meta:
        model = ProfileModel
        fields = '__all__'
