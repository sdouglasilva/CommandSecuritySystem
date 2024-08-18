from django.db import models
from django.contrib.auth.models import User
from items.models import*

# Create your models here.
class Users(models.Model):
  pass
class Staff(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dispositivo = models.ManyToManyField(Devices, related_name='funcionarios')
    equipamento = models.ManyToManyField(Equipments, related_name='funcionarios')
    veiculos = models.ManyToManyField(Vehicles, related_name='funcionarios')