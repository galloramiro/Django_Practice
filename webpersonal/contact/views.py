from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm



class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '?ok'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
