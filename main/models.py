from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    codigo = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    url = models.URLField(blank=True)  # Podría estar en blanco
    codigo_padre = models.CharField(max_length=10, blank=True)  # Podría estar en blanco

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    codigo = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    url = models.URLField(blank=True)  # Podría estar en blanco
    codigo_padre = models.CharField(max_length=10, blank=True)  # Podría estar en blanco
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    codigo = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    url = models.URLField(blank=True)  # Podría estar en blanco
    codigo_padre = models.CharField(max_length=10, blank=True)  # Podría estar en blanco
    provincia = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EstadoCivil(models.Model):
    descripcion_estado_civil = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.descripcion_estado_civil

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    numrut_cliente = models.CharField(max_length=11, primary_key=True)
    dvrut_cliente = models.CharField(max_length=2)
    telefono_cliente = models.CharField(max_length=15)
    direccion_cliente = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)

    def __str__(self):
        return self.numrut_cliente

class Sucursal(models.Model):
    nombre_clinica = models.CharField(max_length=50)
    direccion_clinica = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_clinica


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_especialidad

class Veterinario(models.Model):
    numrut_veterinario = models.CharField(max_length=11, primary_key=True)
    dvrut_veterinario = models.CharField(max_length=2)
    nombre_veterinario = models.CharField(max_length=50)
    apellido_veterinario = models.CharField(max_length=50)
    direccion_veterinario = models.CharField(max_length=50)
    telefono_veterinario = models.CharField(max_length=15)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_veterinario} {self.apellido_veterinario}"
 

class Recepcionista(models.Model):
    numrut_recepcionista = models.CharField(max_length=11, primary_key=True)
    dvrut_recepcionista = models.CharField(max_length=2)
    nombre_recepcionista = models.CharField(max_length=50)
    apellido_recepcionista = models.CharField(max_length=50)
    direccion_recepcionista = models.CharField(max_length=50)
    telefono_recepcionista = models.CharField(max_length=15)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_recepcionista} {self.apellido_recepcionista}"

class RazaPaciente(models.Model):
    raza_paciente = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.raza_paciente

class TipoPaciente(models.Model):
    tipo_paciente = models.CharField(max_length=50)
    raza_paciente = models.ForeignKey(RazaPaciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_paciente

class Tratamiento(models.Model):
    tipo_tratamiento = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo_tratamiento

class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=50)
    sexo_paciente = models.BooleanField(choices=[(True, 'Masculino'), (False, 'Femenino')])
    fecha_nacimiento_paciente = models.DateField()
    color_paciente = models.CharField(max_length=25)
    observacion_paciente = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_paciente = models.ForeignKey(TipoPaciente, on_delete=models.CASCADE)  
    tipo_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)  

    def __str__(self):
        return self.nombre_paciente