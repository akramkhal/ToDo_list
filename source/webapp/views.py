from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    context = {
        'tasks': Task.objects.all().order_by('-id')
    }
    return render(request, 'index.html', context)


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description', '').strip()
        status = request.POST.get('status', 'new')
        due_date = request.POST.get('due_date', '').strip()

        errors = []
        if not description:
            errors.append('Описание обязательно.')
        if status not in dict(STATUS_CHOICES):
            errors.append('Неверный статус.')
        if due_date:
            try:
                date.fromisoformat(due_date)
            except ValueError:
                errors.append('Дата должна быть в формате YYYY-MM-DD, например 2021-12-19.')
        else:
            due_date = None

        if errors:
            context = {
                'status_choices': STATUS_CHOICES,
                'errors': errors,
                'description': description,
                'status': status,
                'due_date': due_date or '',
            }
            return render(request, 'create_task.html', context)

        Task.objects.create(description=description, status=status, due_date=due_date)
        return redirect('/')


def task_delete_view(request):
    if request.method == 'POST':
        task_id = request.GET.get('id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('/')
