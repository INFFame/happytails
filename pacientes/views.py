# pacientes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            return redirect('ver_paciente')  # Ajusta esto según tu URL de redirección
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

@login_required
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, cliente=request.user.cliente)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado con éxito.')
        return redirect('ver_paciente')
    return render(request, 'confirmar_eliminar.html', {'paciente': paciente})