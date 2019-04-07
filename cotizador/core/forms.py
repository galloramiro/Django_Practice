from django import forms
from django.shortcuts import redirect, reverse

COUPLE_CHOICES = [('no','Idividual'), ('yes','Matrimonio'),]
KIDS_CHOICES = [(0, 'Sin hijos'), (1, '1 Hijo'), (2, '2 Hijos'), (3, '3 Hijos'), (4, '4 Hijos'), (5, '5 Hijos'), (6, '6 Hijos') ]

class QuoteForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget= forms.TextInput(
                           attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
                          ), min_length=3, max_length=100)
    couple = forms.CharField(label='', required=True, widget = forms.Select(choices=COUPLE_CHOICES, 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Pareja'}
                            ))
    age = forms.IntegerField(label='Edad', required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Edad'}
                            ))
    age_couple = forms.IntegerField(label='Edad Pareja', required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Edad Pareja'}
                            ))
    kids = forms.CharField(label='Hijos', required=True, widget = forms.Select(choices=KIDS_CHOICES, 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Hijos'}
                            ))
    k_age1 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} ))
    k_age2 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} ))
    k_age3 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} ))
    k_age4 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} ))
    k_age5 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} ))
    k_age6 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} 
                            ))
    salary = forms.FloatField(label='Salario', required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Salario'}
                            ))
    fam_charge = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Familiar a cargo'}
                            ))
    fam_charge_a1 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} ))
    fam_charge_a2 = forms.IntegerField(required=True, widget = forms.NumberInput( 
                              attrs={'class':'form-control', 'rows': 5, 'value': 0} ))





