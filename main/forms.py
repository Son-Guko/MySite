from django import forms

class Createnewlist(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    check = forms.BooleanField(required=False)
