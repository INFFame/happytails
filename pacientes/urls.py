from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_editar_paciente, name='crear_paciente'),
    path('editar/<int:id>/', views.crear_editar_paciente, name='editar_paciente'),
]
