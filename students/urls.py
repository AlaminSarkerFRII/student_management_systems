from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>' , views.view_student , name='view_student')
    # path('students/register/', students.views.register, name='register'),
    # path('students/login/', students.views.login, name='login'),
]
