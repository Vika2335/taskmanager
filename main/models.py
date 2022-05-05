from django.db import models


class Task(models.Model):
    title = models.CharField('Лошара', max_length=50)
    task = models.TextField('СуперЛох', max_length=50)

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Задача"
        verbose_name_plural = "Задачi"


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name