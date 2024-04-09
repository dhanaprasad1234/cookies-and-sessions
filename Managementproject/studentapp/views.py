from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

def show(request):
    form=StudentForm()
    context={'form':form}
    return render(request,'index.html',context)
# Create your views here.
def create (request):
    if request.method == 'POST':
        form=StudentForm(request.POST,request.FILES)

        if form.is_valid():
            student_id=form.cleaned_data['student_id']
            student_name = form.cleaned_data['student_name']
            print(form.cleaned_data['student_name'])
            student_attendence=form.cleaned_data['student_attendence']
            student_Email=form.cleaned_data['student_Email']
            student_contactNo=form.cleaned_data['student_contactNo']
            Student_gender=form.cleaned_data['Student_gender']
            student_Course=form.cleaned_data['student_Course']
            student_photo=form.cleaned_data['student_photo']
            print(form.cleaned_data['student_photo'])
            student_assignment=form.cleaned_data['student_assignment']
            # form.save()
            student=Student(student_id,student_name,student_attendence,student_Email,student_contactNo,Student_gender,student_Course,student_photo,student_assignment)
            student.save()
            return redirect('visual')
        else:
            form=StudentForm()
        return redirect('show/',{'form':form})

def visual(request):
    form=Student.objects.all()
    return render(request, 'success.html',{'form':form})


