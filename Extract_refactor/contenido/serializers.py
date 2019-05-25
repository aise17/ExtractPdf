
from rest_framework import serializers
from .models import AnuncioInferior, AnuncioSuperior, AnuncioLateral, QuienSomos, Bono, Explicacion


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


class BonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bono
        fields = "__all__"




class QuienSomosSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienSomos
        fields = "__all__"


class ExplicaionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Explicacion
        fields = "__all__"


class FaqsSerializer(serializers.ModelSerializer):

    class Meta:
        model= Explicacion
        fields = "__all__"