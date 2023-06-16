from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

from .forms import TodoForm
from .models import Task


class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'


class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']

    success_url ="/"

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = "/"

def task_add(request):
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task1 = Task(name=name, priority=priority, date=date)
        task1.save()
        return redirect('/')
    return render(request, 'add.html')


def tasksindex(request):
    task = Task.objects.all()
    return render(request, 'index.html', {'task': task})


def deletee(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, request.FILES, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})
