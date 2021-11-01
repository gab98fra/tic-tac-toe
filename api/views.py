from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from juego.models import PartidaModel, OpcionModel
from api.serializers import PartidaSerializer, OptionSerializer


class PartidaView(APIView):
    
    def get(self, request, *args, **kwargs):

        partida=PartidaModel.objects.all()
        serializer=PartidaSerializer(partida, many=True)
        
        return Response(serializer.data)


class API_TemplateView(TemplateView):
    
    template_name="api/partida.html"


