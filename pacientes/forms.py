from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre_paciente', 'sexo_paciente', 'fecha_nacimiento_paciente', 'color_paciente', 'observacion_paciente', 'tipo_paciente', 'tipo_tratamiento']
        labels = {
            'nombre_paciente': 'Nombre del Paciente',
            'sexo_paciente': 'Sexo',
            'fecha_nacimiento_paciente': 'Fecha de Nacimiento',
            'color_paciente': 'Color',
            'observacion_paciente': 'Observaciones',
            'tipo_paciente': 'Tipo de Paciente',
            'tipo_tratamiento': 'Tipo de Tratamiento',
        }