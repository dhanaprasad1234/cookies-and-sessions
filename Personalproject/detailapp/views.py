from django.shortcuts import render
from .models import Details
from .forms import DetailsForm

# Create your views here.
# def index(request):
#     forms=DetailsForm()
#     return render(request, 'index.html',{'forms':forms})

def save(request):
    if request.method == 'POST':
        form=DetailsForm (request.POST)
        if form.is_valid():

            ID=form.cleaned_data.get('ID')
            student_name=form.cleaned_data['student_name']
            student_attendence=form.cleaned_data['student_attendence']
            student_Email = form.cleaned_data['student_Email']
            student_contactNo = form.cleaned_data['student_contactNo']
            details=Details(ID,student_name,student_attendence,student_Email,student_contactNo)
            details.save()
            return render(request,'success.html')
    else:
        form=DetailsForm()
    return render(request,'index.html',{'form':form})
    # return redirect('index',{'forms':forms})




