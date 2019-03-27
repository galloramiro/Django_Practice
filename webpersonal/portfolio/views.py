from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Project
# Create your views here.

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'description','image']
    success_url = reverse_lazy('projects:project-list')