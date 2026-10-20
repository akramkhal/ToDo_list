from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, null=False, blank=False, choices=STATUS_CHOICES, default='new',
                              verbose_name="Статус")
    due_date = models.DateField(null=True, blank=True, default=None, verbose_name="Дата выполнения")

    def __str__(self):
        return f'{self.pk} - {self.description}'

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
