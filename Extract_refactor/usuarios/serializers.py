from rest_framework import serializers
from django.contrib.auth.models import User

import sys
sys.path.append("..")

from contenido.models import Bono
from ocr_api.models import File, IpsFiles
from .models import Incidencia, BonoUsuario, MarketingCampaign


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'is_staff')

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.set_password(validated_data.get('password', instance.password))
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return validated_data


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



class IncidenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = "__all__"


class BonoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonoUsuario
        fields = "__all__"

    def update(self, instance, validated_data):

        instance.id = validated_data.get('id', instance.id)
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.bono = validated_data.get('bono', instance.bono)
        instance.activado = validated_data.get('activado', instance.activado)
        instance.peticiones_restantes = validated_data.get('peticiones_consumidas', instance.peticiones_consumidas)

        instance.save()

        return instance, validated_data

    def create(self, validated_data):
        instance = BonoUsuario()
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.bono = validated_data.get('bono', instance.bono)
        instance.activado = validated_data.get('activado', instance.activado)
        instance.peticiones_restantes = self.peticomesByBono(validated_data.get('bono').id)

        instance.save()

        return instance


    def peticomesByBono(self, id):

        queryset = Bono.objects.all()
        obj =queryset.get(id=id)
        num = obj.peticiones

        return int(num)


class MarketingCampaignSerializers(serializers.ModelSerializer):
    class Meta:
        model = MarketingCampaign
        fields = "__all__"





