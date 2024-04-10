from django.shortcuts import render
from .forms import NameForm,MotherForm,FatherForm
# Create your views here.

def name_view(request):
    form = NameForm()
    return render(request,'name.html',{'form':form})

def father_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = FatherForm()
    return render(request,'father.html',{'form':form})

def mother_view(request):
    father = request.GET['father']
    request.session['father'] = father
    form = MotherForm()
    return render(request,'mother.html',{'form':form})

def result_view(request):
    mother = request.GET['mother']
    request.session['mother'] = mother
    return render(request,'result.html')