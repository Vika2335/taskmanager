from .models import Task, City
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи название'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введи описание'
            })
        }


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'name': 'city',
                'id': 'city',
                'placeholder': 'Введите город'
            })
        }