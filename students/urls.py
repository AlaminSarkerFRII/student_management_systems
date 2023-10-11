from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>' , views.view_student , name='view_student'),
    path('add/', views.add, name = 'add')
]
