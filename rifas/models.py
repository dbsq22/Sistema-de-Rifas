from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField(unique=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.numero}"

class NumeroDisponible(models.Model):
    numero = models.IntegerField(unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Numero: {self.numero}, Disponible: {self.disponible}"