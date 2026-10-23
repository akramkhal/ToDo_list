from django.contrib import admin
from webapp.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'due_date')
    list_filter = ('status',)
    search_fields = ('description',)
    fields = ('id', 'description', 'detailed_description', 'status', 'due_date')
    readonly_fields = ('id',)
