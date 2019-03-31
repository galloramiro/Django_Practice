from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from portfolio.views import StaffRequiredMixin
from .forms import AboutForm
from .models import About
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'core/home.html'


class AboutListlView(ListView):
    model = About


class AboutUpdate(StaffRequiredMixin, UpdateView):
    model = About
    form_class = AboutForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id]) + '?ok'


class ContactPageView(TemplateView):
    template_name = 'core/contact.html'


