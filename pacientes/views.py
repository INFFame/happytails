# pacientes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from .forms import PacienteForm

def crear_editar_paciente(request, id=None):
    if id:
        paciente = get_object_or_404(Paciente, id=id)
    else:
        paciente = Paciente()

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.cliente = request.user.cliente  # Asumiendo que tienes una relación con el cliente logueado
            paciente.save()
            return redirect('index')
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/crear_editar_paciente.html', {'form': form})
