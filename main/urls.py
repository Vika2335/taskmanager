from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('dop', views.dop, name='dop'),
    path('pol', views.pol, name='pol')
]