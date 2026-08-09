from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
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
    fields = ['title', 'description', 'status', 'priority', 'due_date']
    success_url = reverse_lazy('tasks:task-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
    success_url = reverse_lazy('tasks:task-list')



class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks:task-list')

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task-list')
