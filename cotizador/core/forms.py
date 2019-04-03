from django import forms
from django.shortcuts import redirect, reverse

AGE_CHOICES = [('jr', '-25 años'), ('juv', '26-35 años'), ('ind', '35+ años'), ]
COUPLE_CHOICES = [('yes','Matrimonio'),('no','Idividual')]
KIDS_CHOICES = [(0, 'Sin hijos'), (1, '1 Hijo'), (2, '2 Hijos'), (3, '3 Hijos'), (4, '4 Hijos'), (5, '5 Hijos'), (6, '6 Hijos'), (7, '7 Hijos') ]

class QuoteForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget= forms.TextInput(
                           attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
                          ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget= forms.EmailInput(
                             attrs={'class':'form-control', 'placeholder':'Escribe tu email ejemplo@ejemplo.com'}
                            ), min_length=3, max_length=100)
    couple = forms.CharField(label='Edad', required=True, widget = forms.Select(choices=COUPLE_CHOICES, 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Pareja'}
                            ))
    age = forms.CharField(label='Edad', required=True, widget = forms.Select(choices=AGE_CHOICES, 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Edad'}
                            ))
    kids = forms.CharField(label='Edad', required=True, widget = forms.Select(choices=KIDS_CHOICES, 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Kids'}
                            ))
    salary = forms.FloatField(label='Edad', required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Salario'}
                            ))




