from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

class TaskCreateView(CreateView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_create.html'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'

class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_update.html'

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_delete.html'
