from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS_CHOICES
from webapp.forms import TaskForm


def index_view(request):
    context = {
        'tasks': Task.objects.all().order_by('-id')
    }
    return render(request, 'index.html', context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            detailed_description = form.cleaned_data.get('detailed_description')
            status = form.cleaned_data.get('status')
            due_date = form.cleaned_data.get('due_date')
            task = Task.objects.create(description=description, detailed_description=detailed_description, status=status, due_date=due_date)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create_task.html', {'form': form})

def task_delete_view(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
    return redirect('index')
