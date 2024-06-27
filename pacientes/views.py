# pacientes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PacienteForm
from .models import Paciente

def crear_editar_paciente(request, id=None):
    if id:
        paciente = get_object_or_404(Paciente, id=id)
    else:
        paciente = Paciente()

    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.cliente = request.user.cliente  # Asocia el cliente al paciente
            paciente.save()
            return redirect('index')  # Ajusta esto según tu URL de redirección
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/crear_editar_paciente.html', {'form': form})

def ver_paciente(request):
    cliente = request.user.cliente  # Asegúrate de que el cliente esté asociado al usuario
    pacientes = Paciente.objects.filter(cliente=cliente)

    context = {
        'pacientes': pacientes,
    }

    return render(request, 'pacientes/ver_paciente.html', context)