from django.db import models

# Create your models here.



class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=100)
    gpa = models.FloatField()
    email = models.EmailField(max_length=100, null=True , blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)


    class Meta:
         db_table = 'students_info'
         verbose_name_plural = 'students'



    def __str__(self) -> str:
        return f'Students :{self.fisrt_name} {self.last_name}'