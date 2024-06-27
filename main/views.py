from roll.models import TipoUsuario
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from .models import Cliente
from agenda.models import Cita

def base(request):
    return render(request, "base.html")


def index(request):
    # Obtener el TipoUsuario asociado al usuario actual si está autenticado
    tipo_usuario = None
    if request.user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=request.user)
        except TipoUsuario.DoesNotExist:
            pass
    
    context = {
        'tipo_usuario': tipo_usuario.tipo if tipo_usuario else None
    }
    
    return render(request, 'index.html', context)


def servicios(request):
    # Obtener el TipoUsuario asociado al usuario actual si está autenticado
    tipo_usuario = None
    if request.user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=request.user)
        except TipoUsuario.DoesNotExist:
            pass
    
    # Pasar el tipo de usuario al contexto de la plantilla
    context = {
        'tipo_usuario': tipo_usuario.tipo if tipo_usuario else None
    }
    
    return render(request, "servicios.html", context)


def nosotros(request):
    # Obtener el TipoUsuario asociado al usuario actual si está autenticado
    tipo_usuario = None
    if request.user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=request.user)
        except TipoUsuario.DoesNotExist:
            pass
    
    # Pasar el tipo de usuario al contexto de la plantilla
    context = {
        'tipo_usuario': tipo_usuario.tipo if tipo_usuario else None
    }
    return render(request, "nosotros.html", context)


def contacto(request):
    # Obtener el TipoUsuario asociado al usuario actual si está autenticado
    tipo_usuario = None
    if request.user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=request.user)
        except TipoUsuario.DoesNotExist:
            pass
    
    # Pasar el tipo de usuario al contexto de la plantilla
    context = {
        'tipo_usuario': tipo_usuario.tipo if tipo_usuario else None
    }
    return render(request, "contacto.html", context)


@login_required
def editar_cliente(request):
    # Obtener el TipoUsuario asociado al usuario actual
    try:
        tipo_usuario = TipoUsuario.objects.get(usuario=request.user)
    except TipoUsuario.DoesNotExist:
        tipo_usuario = None
    
    try:
        cliente = get_object_or_404(Cliente, usuario=request.user)
    except Cliente.DoesNotExist:
        return render(request, 'editar_cliente.html', {'message': 'No se encontró un cliente asociado a este usuario.'})

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return render(request, 'editar_cliente.html', {'form': form, 'success': True})
    else:
        form = ClienteForm(instance=cliente)

    # Pasar el tipo de usuario al contexto de la plantilla
    context = {
        'tipo_usuario': tipo_usuario.tipo if tipo_usuario else None,
        'form': form
    }

    return render(request, 'editar_cliente.html', context)

@login_required
def citas(request):
    # Obtener el TipoUsuario asociado al usuario actual si está autenticado
    tipo_usuario = None
    if request.user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=request.user)
        except TipoUsuario.DoesNotExist:
            pass
    
    # Recuperar las citas del usuario autenticado
    citas = Cita.objects.filter(usuario=request.user)
    
    # Pasar el tipo de usuario y las citas al contexto de la plantilla
    context = {
        'tipo_usuario': tipo_usuario.tipo if tipo_usuario else None,
        'citas': citas
    }
    
    return render(request, 'citas.html', context)
