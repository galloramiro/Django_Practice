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
        r_get = self.request.GET
        d_get = {'name': None , 'email':None , 'couple': None, 'age': None, 'kids':None ,}
        
        for value in d_get:
            d_get[value] = r_get[value]

        query_filter = Quotes().planSelector(d_get['couple'], d_get['kids'], d_get['age'])


        queryset = super(QuoteListView, self).get_queryset().filter(composite=query_filter)
        return queryset


