from django import forms
from .models import Document 


class DocumentForm(forms.ModelForm): 
    class Meta: 
        model = Document 
        fields = ('title', 'uploaded_file',)


class Createnewlist(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    check = forms.BooleanField(required=False)
