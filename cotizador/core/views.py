from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import QuoteForm
from .models import SmgQuotesTable
from .quotes import Quotes


class QuoteFormView(FormView):
    template_name = 'core/home.html'
    form_class = QuoteForm
    success_url = 'quotes'

    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        couple = form.cleaned_data['couple']
        age = form.cleaned_data['age']
        kids = form.cleaned_data['kids']
        #query_filter = Quotes().planSelector(couple, kids, age)
        #obj = SmgQuotesTable.objects.filter(composite='Ind. Junior (H25)')
        return super(QuoteFormView, self).form_valid(form)


class QuoteView(TemplateView, QuoteFormView):
    template_name = "core/quotes.html"

    
    def get_queryset(self):
        queryset = super(CLASS_NAME, self).get_queryset()
        queryset = queryset # TODO
        return queryset


