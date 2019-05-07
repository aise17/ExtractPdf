
from rest_framework import serializers
from .models import AnuncioInferior, AnuncioSuperior, AnuncioLateral





class AnuncioLateralSerializer(serializers.ModelSerializer):

    class Meta:
        model= AnuncioLateral
        fields = "__all__"


class AnuncioSuperiorSerializer(serializers.ModelSerializer):

    class Meta:
        model= AnuncioSuperior
        fields = "__all__"


class AnuncioInferiroSerializer(serializers.ModelSerializer):

    class Meta:
        model= AnuncioInferior
        fields = "__all__"
