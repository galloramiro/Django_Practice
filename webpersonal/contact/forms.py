from django import forms
from django.core.mail import EmailMessage
from django.shortcuts import redirect, reverse

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget= forms.TextInput(
                           attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
                          ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget= forms.EmailInput(
                             attrs={'class':'form-control', 'placeholder':'Escribe tu email ejemplo@ejemplo.com'}
                            ), min_length=3, max_length=100)
    content = forms.CharField(label='Contenido', required=True, widget = forms.Textarea(
                              attrs={'class':'form-control', 'rows': 5, 'placeholder': 'Escribime tu mensaje que a la brevedad me pondré en contacto con vos'}
                            ))

    def send_email(self):
        name = self.cleaned_data['name']
        mail = self.cleaned_data['email']
        content = self.cleaned_data['content']

        email = EmailMessage('[Ramiro Gallo] Nuevo mensaje de contacto',
                'De {} <{}> \n\nEscribió:\n\n{}'.format(name, mail, content),
                'ramiro.r.gallo@gmail.com',
                ['ramiro.r.gallo@gamil.com'],
                reply_to=[mail]
                )

        email.send(fail_silently=True)
        return redirect(reverse('contact')+'?ok')
