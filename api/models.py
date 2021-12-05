from django.db import models


# Create your models here.

class APImodel(models.Model):
    
    id=models.AutoField(primary_key=True)
    campo1=models.CharField(max_length=100)
    campo2=models.IntegerField()
    estado=models.BooleanField(default=True)
