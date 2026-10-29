from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=3000, required=True, widget=widgets.Textarea(attrs={'class': 'form-control', 'rows': 3}), label="Описание")
    detailed_description = forms.CharField(max_length=3000, required=False, widget=widgets.Textarea(attrs={'class': 'form-control', 'rows': 3}), label="Подробное описание")
    status = forms.ChoiceField(choices = STATUS_CHOICES, initial=STATUS_CHOICES[0][0], widget=widgets.Select(attrs={'class': 'form-select'}), label="Статус")
    due_date = forms.DateField(required=False, input_formats=['%Y-%m-%d'],
                               widget=widgets.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}), label="Дата выполнения")
