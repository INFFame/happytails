from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from .models import Cliente
from agenda.models import Cita

# Create your views here.

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def servicios(request):
    return render(request, "servicios.html")

def nosotros(request):
    return render(request, "nosotros.html")

def contacto(request):
    return render(request, "contacto.html")

@login_required
def editar_cliente(request):
    try:
        cliente = get_object_or_404(Cliente, usuario=request.user)
    except Cliente.DoesNotExist:
        return render(request, 'editar_cliente.html', {'message': 'No se encontró un cliente asociado a este usuario.'})

    if request.method == 'POST':
        # Al pasar instance=cliente al formulario, nos aseguramos de que estamos actualizando el objeto existente
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Renderizar la misma página después de guardar los cambios
            return render(request, 'editar_cliente.html', {'form': form, 'success': True})
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form})

@login_required
def citas(request):
    # Recuperar las citas del usuario autenticado
    citas = Cita.objects.filter(usuario=request.user)
    return render(request, 'citas.html', {'citas': citas})