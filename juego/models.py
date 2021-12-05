from django.db import models
from django.contrib.auth.models import User


class PartidaModel(models.Model):
    "Partida de juego"
    
    id=models.AutoField(primary_key=True)
    estado=models.BooleanField(default=False)
    ganador=models.CharField(max_length=50, null=True, blank=True)
    created=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


class OpcionModel(models.Model):
    "Opciones selecciondas en una partida"
    
    id=models.AutoField(primary_key=True)
    opcion=models.IntegerField()
    created=models.DateField(auto_now_add=True)
    user=models.CharField(max_length=30)
    partida=models.ForeignKey(PartidaModel, on_delete=models.CASCADE)


class ArhivoCargar(models.Model):
    
    id=models.AutoField(primary_key=True)
    img=models.ImageField()