from django.shortcuts import render, HttpResponseRedirect
from .forms import Registeration
from .models import User

# Create your views here.

# This function will Add & Show the data. 
def add_show(request):
    if request.method == 'POST':
        fm = Registeration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = Registeration()
    else:
        fm = Registeration()
    stud = User.objects.all()

    return render(request,'addandshow.html', {'form':fm, 'stu':stud})

# This function will Update(Edit) the data

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Registeration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = Registeration(instance=pi)
    return render(request, 'updatest.html', {'form':fm})

# This function will Add & Show the data. 
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id) 
        pi.delete()
        return HttpResponseRedirect('/')