from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Guia
from .forms  import GuiaForm

guias = []

def crear_guia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        tema = request.POST.get('tema')
        if titulo and tema:
            guia = {'id': len(guias) + 1, 'title': titulo, 'tema': tema, 'resources': ''}
            guias.append(guia)
            return redirect('listar_guias')
    return render(request, 'crear_guia.html')

def listar_guias(request):
    if request.method == 'POST':
        gid = int(request.POST.get('id'))
        recurso = request.POST.get('resources')
        for guia in guias:
            if guia['id'] == gid:
                guia['resources'] = recurso
                break
    return render(request, 'revisar_guias.html', {'guias': guias})

def consultar_guias(request):
    return render(request, 'consultar_guias.html', {'guias': guias})

def asignar_recursos(request):
    return redirect('listar_guias')

def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['action'] = 'Crear' if self.request.path.endswith('nueva/') else 'Editar'
    return ctx

class GuiaListView(LoginRequiredMixin, ListView):
    model = Guia
    template_name = 'guia/guia_list.html'
    context_object_name = 'guias'

class GuiaCreateView(LoginRequiredMixin, CreateView):
    model = Guia
    form_class = GuiaForm
    template_name = 'guia/guia_form.html'
    success_url = reverse_lazy('guia:guia_list')

    def form_valid(self, form):
        form.instance.profesor = self.request.user
        return super().form_valid(form)

class GuiaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Guia
    form_class = GuiaForm
    template_name = 'guia/guia_form.html'
    success_url = reverse_lazy('guia:guia_list')

    def test_func(self):
        guia = self.get_object()
        return guia.profesor == self.request.user or self.request.user.is_staff

class GuiaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Guia
    template_name = 'guia/guia_confirm_delete.html'
    success_url = reverse_lazy('guia:guia_list')

    def test_func(self):
        guia = self.get_object()
        return guia.profesor == self.request.user or self.request.user.is_staff
