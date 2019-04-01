from django import forms
from django.shortcuts import redirect, reverse

class QuoteForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget= forms.TextInput(
                           attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
                          ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget= forms.EmailInput(
                             attrs={'class':'form-control', 'placeholder':'Escribe tu email ejemplo@ejemplo.com'}
                            ), min_length=3, max_length=100)
    content = forms.CharField(label='Contenido', required=True, widget = forms.Textarea(
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Escribime tu mensaje que a la brevedad me pondré en contacto con vos'}
                            ))


