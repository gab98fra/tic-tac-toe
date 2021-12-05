from rest_framework.serializers import ModelSerializer
from juego.models import PartidaModel, OpcionModel
from .models import APImodel

class PartidaSerializer(ModelSerializer):
    class Meta:
        model=PartidaModel
        fields=['id', 'estado', 'ganador',]



class OptionSerializer(ModelSerializer):
    
    class Meta:
        model=OpcionModel
        fields=['id', 'opcion', 'partida']


class APISerializer(ModelSerializer):

    class Meta:
        model=APImodel
        fields="__all__"
