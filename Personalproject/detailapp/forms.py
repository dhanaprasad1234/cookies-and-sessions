from django import forms
from .models import Details
class DetailsForm (forms.Form):
    student_name = forms.CharField(max_length=225)
    student_attendence = forms.IntegerField()
    student_Email = forms.EmailField(max_length=33)
    student_contactNo = forms.IntegerField()



    def clean_student_name(self):
        student_name=self.cleaned_data['student_name']
        if len(student_name) <= 6:
            raise forms.ValidationError("Name is to long.Please Enter the name below 16 charater")
        return student_name

    def clean_student_attendence(self):
        student_attendence=self.cleaned_data['student_attendence']

        if student_attendence <= 0 or student_attendence > 100:
            raise forms.ValidationError("Attendence of below 100 numbers")
        return student_attendence

    def clean_student_Email(self):
        student_Email=self.cleaned_data['student_Email']
        if len(student_Email) < 4:
            raise forms.ValidationError("please enter the email")
        return student_Email

    def clean_student_contactNo(self):
        student_contactNo=self.cleaned_data['student_contactNo']

        if len(str(student_contactNo)) < 11 :
            raise forms.ValidationError("please enter number  valid ")
        return student_contactNo

