from django.views.generic import CreateView, ListView, DeleteView   
from .models import Cita
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(self.request, "¡Usted no tiene autorización!")
        return redirect("index")
    
class ClienteCreateMixin(LoginRequiredMixin):
    login_url = 'signin'

    def handle_no_permission(self):
        messages.error(self.request, "¡Debe iniciar sesión para agendar una hora!")
        return redirect("signin")    

# Vistas
class CitaCreateView(ClienteCreateMixin, CreateView):
    model = Cita
    template_name = 'agendar_hora.html'
    fields = ['veterinario', 'fecha_cita', 'sucursal', 'horario']
    success_url = reverse_lazy('lista_citas')

    def form_valid(self, form):
        # Asignar el usuario actual al campo 'usuario' del formulario antes de guardarlo
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class CitaListView(ClienteCreateMixin, TestMixinIsAdmin, ListView):
    template_name = 'lista_citas.html'

    def get_queryset(self):
        return Cita.objects.all().order_by('-pk')
    
class CitaDeleteView(TestMixinIsAdmin, ClienteCreateMixin, DeleteView):
    model = Cita
    success_url = reverse_lazy('cita_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Cita cancelada con éxito!")
        return reverse_lazy('cita_list')    

cita_create = CitaCreateView.as_view()    
cita_list = CitaListView.as_view()
cita_delete = CitaDeleteView.as_view()