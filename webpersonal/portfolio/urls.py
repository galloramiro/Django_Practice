from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreate

projects_patterns = ([
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('create/', ProjectCreate.as_view(), name='create'),
], 'projects')