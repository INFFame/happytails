from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError, transaction
from .models import TipoUsuario  
from main.models import Cliente
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout
from .forms import RegistroUserForm
import uuid

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': RegistroUserForm()})
    else:
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                try:
                    with transaction.atomic():
                        # Crear el usuario
                        user = User.objects.create_user(
                            username=request.POST['username'], 
                            first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            email=request.POST['email'], 
                            password=request.POST['password1']
                        )
                        print(f"User created: {user}")

                        # Asociar al grupo "Clientes" (suponiendo que ya existe)
                        grupo, _ = Group.objects.get_or_create(name='Clientes')
                        user.groups.add(grupo)
                        print(f"User added to group 'Clientes'")

                        # Crear el tipo de usuario asociado (en este caso, cliente)
                        tipo = TipoUsuario.objects.create(usuario=user, tipo='cliente')
                        tipo.save()
                        print(f"TipoUsuario created: {tipo}")

                        # Crear el cliente
                        numrut_cliente = str(uuid.uuid4())[:12]  # Generar un UUID único y truncarlo a 12 caracteres
                        cliente = Cliente.objects.create(
                            usuario=user,
                            numrut_cliente=numrut_cliente,
                            telefono_cliente=None,
                            direccion_cliente='',
                            comuna=None,
                            estado_civil=None
                        )
                        cliente.save()
                        print(f"Cliente created: {cliente}")

                    # Cerrar la sesión actual del usuario
                    django_logout(request)

                    # Redirigir a la misma página para limpiar los datos POST
                    return HttpResponseRedirect(reverse('index'))
                except IntegrityError as e:
                    print(f"IntegrityError: {e}")
                    return render(request, 'signup.html', {
                        'form': RegistroUserForm(),
                        'error': 'Error al crear el Cliente'
                    })
            else:
                print("Passwords do not match")
                return render(request, 'signup.html', {
                    'form': RegistroUserForm(),
                    'error': 'Las contraseñas no coinciden'
                })
        else:
            print(f"Form errors: {form.errors}")
            return render(request, 'signup.html', {
                'form': form,
                'error': 'Por favor, corrige los errores en el formulario'
            })


def signout(request):
    # Cerrar sesión en Django
    django_logout(request)
    
    # Redirigir al usuario a la página de inicio
    response = redirect('index')
    
    # Eliminar csrftoken si está presente
    if 'csrftoken' in request.COOKIES:
        response.delete_cookie('csrftoken')
    
    # Eliminar sessionid si está presente
    if 'sessionid' in request.COOKIES:
        response.delete_cookie('sessionid')

    # Eliminar messages si está presente
    if 'messages' in request.COOKIES:
        response.delete_cookie('messages')

    return response



def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña es incorrecta'})
        else:
            login(request, user)
            return redirect('index')
