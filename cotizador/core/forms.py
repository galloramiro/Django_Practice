from django import forms
from django.shortcuts import redirect, reverse

AGE_CHOICES= [('-25', '-25'), ('26-35', '26-35'), ('35+', '35+'), ]
KIDS_CHOICES= [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), ]

class QuoteForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget= forms.TextInput(
                           attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
                          ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget= forms.EmailInput(
                             attrs={'class':'form-control', 'placeholder':'Escribe tu email ejemplo@ejemplo.com'}
                            ), min_length=3, max_length=100)
    age = forms.CharField(label='Edad', required=True, widget = forms.Select(choices=AGE_CHOICES, 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Edad'}
                            ))
    kids = forms.CharField(label='Edad', required=True, widget = forms.Select(choices=KIDS_CHOICES, 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Kids'}
                            ))




