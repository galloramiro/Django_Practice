from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import QuoteForm
from .models import SmgQuotesTable
from .quotes import Quotes


class QuoteFormView(FormView):
    template_name = 'core/home.html'
    form_class = QuoteForm
    success_url = 'quotes'



class QuoteListView(ListView):
    model = SmgQuotesTable

    def get_queryset(self):
        r_get = self.request.GET   # Get the data sendir by QuoteFormView
        query_filter = Quotes().planSelector(r_get['couple'], r_get['kids'], r_get['age']) # Use the filter to get the correct Quote
        queryset = super(QuoteListView, self).get_queryset().filter(composite=query_filter) # Aply the filter to get the correct queryset
        Quotes().salaryDiscount(queryset,r_get['salary'])  # Aply the discount of the salary

        return queryset
    

