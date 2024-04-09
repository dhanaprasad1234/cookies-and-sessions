from django import forms
from .models import Student

class StudentForm(forms.Form):

    student_id = forms.IntegerField()
    student_name = forms.CharField(max_length=225)
    student_attendence = forms.IntegerField()
    student_Email = forms.EmailField(max_length=33)
    student_contactNo = forms.IntegerField()
    RADIO_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    Student_gender = forms.ChoiceField(choices=RADIO_CHOICES)
    SELECT_CHOICES = [
        ('Java', 'Java'),
        ('Python', 'Python'),
    ]
    student_Course = forms.ChoiceField(choices=SELECT_CHOICES,widget=forms.RadioSelect)
    student_photo = forms.ImageField()
    student_assignment = forms.FileField()

    # student_description = forms.CharField(widget=forms.Textarea)
    # class Meta:
    #     model=Student
    #     fields='__all__'

