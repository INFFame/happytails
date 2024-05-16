from django.db import models
from main.models import Sucursal, Veterinario, Paciente
from django.contrib.auth.models import User


# Create your models here.

class Cita(models.Model):
    fecha_cita = models.DateField()
    hora_cita = models.TimeField(null=True, blank=True)  # Hora de la cita (opcional)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
