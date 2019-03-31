from django import forms
from .models import About

class AboutForm(forms.ModelForm):


    class Meta:
        model = About
        fields = ['title', 'description','image']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}), 
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'', 
            'description':'',
            'image':'',
        }