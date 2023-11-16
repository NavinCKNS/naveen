from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView

from A1.models import states

class detail(CreateView):
    model=states
    fields=('name','capital','language','population')
    success_url=reverse_lazy('list')
class show(ListView):
    model=states
class delete(DeleteView):
    model=states
    success_url=reverse_lazy('list')
class update(UpdateView):
    templates_name='A1/form.html'
    model=states
    fields='__all__'
    success_url=reverse_lazy('list')

    