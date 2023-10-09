from django.db import models
from server.model import StudentPortalAdmin
# Create your models here.



class Student(StudentPortalAdmin):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    fees = models.IntegerField()


    class Meta :
        db_table = 'student_info'
        verbose_name_plural = 'Student'



class Teacher(StudentPortalAdmin):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

    class Meta :
        db_table = 'teacher_info'
        verbose_name_plural = 'Teacher'