# forms.py
from django import forms
from .models import Cliente

class ReadOnlyTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'readonly': 'readonly'})
        super().__init__(*args, **kwargs)

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer el campo numrut_cliente de solo lectura
        self.fields['numrut_cliente'].widget = ReadOnlyTextInput()