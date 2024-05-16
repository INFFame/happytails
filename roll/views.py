from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import TipoUsuario  
from django.contrib.auth.models import Group

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
                try:
                    # Crear el usuario
                    user = User.objects.create_user(username=request.POST['username'], 
                                                    first_name=request.POST['first_name'],
                                                    last_name=request.POST['last_name'],
                                                    email=request.POST['email'], 
                                                    password=request.POST['password1'])
                    # Asociar al grupo "Cliente" (suponiendo que ya existe)
                    grupo, _ = Group.objects.get_or_create(name='Clientes')
                    user.groups.add(grupo)

                    # Crear el tipo de usuario asociado (en este caso, cliente)
                    tipo_usuario = TipoUsuario.objects.create(usuario=user, tipo='cliente')
                    tipo_usuario.save()
                    user.save()
                    return redirect('signin')
                except IntegrityError:
                    return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'Usuario ya existe'
                    })
        else:
            return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden'})



@login_required
def signout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña es incorrecta'
            })
        else:
            login(request, user)
            return redirect('index')

