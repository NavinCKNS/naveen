from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from app1.forms import StudentModelForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from app1.models import student, teachers
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def ind(request):
    return render(request,"index.html")
def log(request):
    return render(request,"logout.html")
def report(request):
    report=student.objects.all()
    context={"records":report}
    return render(request,"app1/htt.html",context)
# def home(request):
#     return render(request,"index.html")
@login_required
@permission_required('app1.add_student')
def details(request):
    forms=StudentModelForm
    print(forms)
    values={"form":forms}
    if request.method=="POST":
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"app1/add.html",values)
# def delete(request,id):
#     s=student.objects.get(id=id)
#     s.delete()
#     return report(request)
def update(request,id):
    v=student.objects.get(id=id)
    s=StudentModelForm(instance=v)
    a={"form":s}
    if request.method=="POST":
        s=StudentModelForm(request.POST,instance=v)
        if s.is_valid():
            s.save()
    return render(request,'app1/update.html',a)
class values(ListView):
    model=teachers

class insert(CreateView):
    model=teachers
    fields=('name','subject','exp','contact')
class delete1(DeleteView):
    model=teachers
    success_url=reverse_lazy('list1')
class update1(UpdateView):
    templates_name='app1/form.html'
    model=teachers  
    fields=('name','exp','contact')
    success_url=reverse_lazy('list1')



