from django import forms

class NameForm(forms.Form):
    name = forms.CharField()

class FatherForm(forms.Form):
    father = forms.CharField()

class MotherForm(forms.Form):
    mother = forms.CharField()