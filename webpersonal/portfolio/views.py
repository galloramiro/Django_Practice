from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm
# Create your views here.

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects:project-list')

class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('project-detail:update', args=[self.object.id]) + '?ok'


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:project-list')