from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Vinho

class IndexView(ListView):
    models = Vinho
    template_name = 'index.html'
    queryset = Vinho.objects.all()
    context_object_name = 'vinhos'


class CreateVinhoView(CreateView):
    model = Vinho
    template_name = 'vinho_form.html'
    fields = ['nome', 'uvas', 'tipo', 'acucar','safra',
              'nacionalidade','vinicola','reserva','alcool',
              'temperatura','volume','amadurecimento', 'guarda',
              'visual','olfativo','gustativo',]
    success_url = reverse_lazy('index')


class UpdateVinhoView(UpdateView):
    model = Vinho
    template_name = 'vinho_form.html'
    fields = ['nome', 'safra']
    success_url = reverse_lazy('index')


class DeleteVinhoView(DeleteView):
    model = Vinho
    template_name = 'vinho_del.html'
    success_url = reverse_lazy('index')


class DetailsVinhoView(generic.DetailView):
    models = Vinho
    template_name = 'details.html'
    queryset = Vinho.objects.all()
    context_object_name = 'vinho'
