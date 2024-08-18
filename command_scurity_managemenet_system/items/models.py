from django.db import models

# Create your models here.
class Devices(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Equipments(models.Model):
      nome = models.CharField(max_length=100)
      descricao = models.TextField()

class Vehicles(models.Model):
      nome = models.CharField(max_length=100)
      descricao = models.TextField()