from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
# Create your views here.



def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students':students})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'), {'student':student})