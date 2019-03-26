from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'core/home.html'

class AboutPageView(TemplateView):
    template_name = 'core/about.html'

class ContactPageView(TemplateView):
    template_name = 'core/contact.html'