from django.contrib.auth.models import User
from rest_framework import serializers


class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def to_representation(self, instance):
        response = super(CreateUserSerializer, self).to_representation(instance)
        response.pop("password")
        return response
