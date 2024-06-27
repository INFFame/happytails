from django import forms
from .models import Cliente, Comuna, EstadoCivil  

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['numrut_cliente', 'telefono_cliente', 'direccion_cliente', 'comuna', 'estado_civil']
        labels = {
            'numrut_cliente': 'Número de RUT Cliente',
            'telefono_cliente': 'Teléfono',
            'direccion_cliente': 'Dirección',
            'comuna': 'Comuna',
            'estado_civil': 'Estado Civil',
        }

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        # Hacer el campo numrut_cliente de solo lectura
        self.fields['numrut_cliente'].widget.attrs['readonly'] = True
        # Asegúrate de que los campos de ForeignKey usen Select widgets para mostrar nombres
        self.fields['comuna'].queryset = Comuna.objects.all()
        self.fields['estado_civil'].queryset = EstadoCivil.objects.all()