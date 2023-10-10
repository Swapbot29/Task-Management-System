from django.shortcuts import render
from .models import Task
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        result = super(TaskListView, self).get_queryset()

        task_filter = self.request.GET.get('team_member')
        if task_filter:
            result = Task.objects.filter(Q(team_member__icontains=task_filter))
        return result

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_update.html'
    success_url = reverse_lazy('home')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'Task'
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('home')