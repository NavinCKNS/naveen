from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView,DeleteView,UpdateView

from A.models import temp
def home(request):
    return render(request,"A/Home.html")
class temp(CreateView):
    model=temp
    fields=('name','cls')
    success_url=reverse_lazy('list1')
class lit(ListView):
    model=temp
    
