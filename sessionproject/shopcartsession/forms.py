from django import forms
# from .models import Cart
class AddItemForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()