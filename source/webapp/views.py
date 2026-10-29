from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
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


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={'description': task.description, 'detailed_description': task.detailed_description,
                                 'status': task.status, 'due_date': task.due_date})
        return render(request, 'update_task.html', {'task': task, 'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.detailed_description = form.cleaned_data.get('detailed_description')
            task.status = form.cleaned_data.get('status')
            task.due_date = form.cleaned_data.get('due_date')
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update_task.html', {'task': task,'form': form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_task.html', {'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
