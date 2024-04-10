from django.shortcuts import render
from .forms import AddItemForm
# Create your views here.


def add_view(request):
    form = AddItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
        return render(request,'additem.html',{'form':form})
    # else:
    #     return render(request,'additem.html',{'form':form})
def display_view(request):
    return render(request,'displayitem.html')