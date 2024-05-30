from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.numero}"

class NumeroDisponible(models.Model):
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.numero)