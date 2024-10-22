
from rest_framework import serializers
from .models import File, IpsFiles, Traza
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.set_password(validated_data.get('password', instance.password))
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def create(self, validated_data):

        user = User()
        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.set_password(validated_data.get('password', user.password))
        user.email = validated_data.get('email', user.email)

        user.save()
        return user



class ArchivoSerializer(serializers.ModelSerializer):

    class Meta:
        model= File
        fields = "__all__"



class IpsFileSerializers(serializers.ModelSerializer):
    class Meta:
        model= IpsFiles
        fields = "__all__"





class TrazaSerializer(serializers.Serializer):
    class Meta:
        model = Traza
        fields = "__all__"




