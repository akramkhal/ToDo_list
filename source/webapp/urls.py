from django.urls import path
from webapp.views import index_view, task_view, task_create_view, task_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('tasks/add/', task_create_view, name='task_add'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete'),
]
