from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import QuoteForm


class QuoteView(FormView):
    template_name = 'core/home.html'
    form_class = QuoteForm
    success_url = '?ok'

