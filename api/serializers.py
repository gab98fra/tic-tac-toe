from rest_framework.serializers import ModelSerializer
from juego.models import PartidaModel, OpcionModel


class PartidaSerializer(ModelSerializer):
    class Meta:
        model=PartidaModel
        fields=['id', 'estado', 'ganador',]



class OptionSerializer(ModelSerializer):
    class Meta:
        model=OpcionModel
        fields=['id', 'opcion', 'partida']


