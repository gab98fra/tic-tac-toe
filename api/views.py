from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView
from juego.models import PartidaModel, OpcionModel
from api.serializers import PartidaSerializer, OptionSerializer
from .serializers import APISerializer
from .models import APImodel
from .mixins import AccesoMixin
"""
    Documentación: https://www.cdrf.co/
"""

class API_TemplateView(TemplateView):
    "template"

    template_name="api/api.html"

class APIInitView(AccesoMixin , APIView):
    
    def get(self, request):

        api=APImodel.objects.all()
        serializer=APISerializer(api, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        api=APISerializer(data=request.data)
        if api.is_valid():
            api.save()
            return Response(api.data, status=status.HTTP_201_CREATED)
        
        return Response(api.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleApi(APIView):
    "Actualiza y elimina objetos"

    def get(self, request, pk):
        
        api=APImodel.objects.filter(id=pk).first()
        serializers=APISerializer(api)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        "Actualizar registro"

        api=APImodel.objects.filter(id=pk).first()
        serializers=APISerializer(api, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        "Eliminar registro"

        api=APImodel.objects.filter(id=pk).first()
        api.delete()
        return Response({"mensaje":"Eliminado"}, status=status.HTTP_200_OK)

class ListAPi(ListAPIView):
    "Clase para lista objetos"

    serializer_class=APISerializer

    def get_queryset(self):
        
        return APImodel.objects.all()
    
