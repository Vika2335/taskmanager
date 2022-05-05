from django.shortcuts import render, redirect
from .models import Task, City
from .forms import TaskForm, CityForm
import requests

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Ульяна лоХУИшка', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def dop(request):
    return render(request, 'main/dop.html', {'title': 'Что хочу'})


def pol(request):
    appid = 'a34d91e2deefb84f4dbc76e99ac5f31f'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = cityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'main/pol.html', context)


def cal(request):
    return render(request, 'main/cal.html', {'title': 'Калькулятор'})


def mus(request):
    return render(request, 'main/mus.html', {'title': 'Музыка'})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)