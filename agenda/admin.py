from django.contrib import admin
from .models import HorarioVeterinario, Cita
from django.forms.widgets import TimeInput
from django import forms

# Define el formulario personalizado para el HorarioVeterinario
class HorarioVeterinarioForm(forms.ModelForm):
    class Meta:
        model = HorarioVeterinario
        fields = '__all__'
        widgets = {
            'hora_inicio_manana': TimeInput(format='%H:%M'),
            'hora_fin_manana': TimeInput(format='%H:%M'),
            'hora_inicio_tarde': TimeInput(format='%H:%M'),
            'hora_fin_tarde': TimeInput(format='%H:%M'),
        }

# Define la clase HorarioVeterinarioAdmin
@admin.register(HorarioVeterinario)
class HorarioVeterinarioAdmin(admin.ModelAdmin):
    actions = ['duplicar_horarios']
    form = HorarioVeterinarioForm  # Utiliza el formulario personalizado

    def duplicar_horarios(self, request, queryset):
        for horario in queryset:
            # Crea una copia del horario veterinario
            horario.pk = None  # Establece la clave primaria en None para crear una nueva entrada
            horario.save()

    duplicar_horarios.short_description = "Duplicar horarios seleccionados"

    list_display = ('veterinario', 'dia_semana', 'hora_inicio_manana', 'hora_fin_manana', 'hora_inicio_tarde', 'hora_fin_tarde')
    list_filter = ('veterinario', 'dia_semana')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Configura los widgets para mostrar la hora como tipo 'time'
        form.base_fields['hora_inicio_manana'].widget.input_type = 'time'
        form.base_fields['hora_fin_manana'].widget.input_type = 'time'
        form.base_fields['hora_inicio_tarde'].widget.input_type = 'time'
        form.base_fields['hora_fin_tarde'].widget.input_type = 'time'
        return form

# Registra el modelo Cita en el administrador de Django
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):    
    pass