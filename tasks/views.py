from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm, TaskFilterForm

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'
    form_class = TaskFilterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.form_class(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['status']:
                queryset = queryset.filter(status=form.cleaned_data['status'])
            if form.cleaned_data['priority']:
                queryset = queryset.filter(priority=form.cleaned_data['priority'])
        return queryset

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_create.html'
    fields = ['title', 'description', 'status', 'priority', 'due_date']
    success_url = reverse_lazy('tasks:task-list')
    login_url = 'admin:login'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'


class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_update.html'
    fields = ['title', 'description', 'status', 'priority', 'due_date']
    success_url = reverse_lazy('tasks:task-list')

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task-list')
