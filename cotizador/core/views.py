from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import QuoteForm


class QuoteView(FormView):
    template_name = 'core/home.html'
    form_class = QuoteForm
    success_url = '?ok'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        age = form.cleaned_data['age']
        kids = age = form.cleaned_data['kids']

    
        return super(QuoteView, self).form_valid(form)

