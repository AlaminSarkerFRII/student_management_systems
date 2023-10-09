from django.contrib import admin
from .models import Student , Teacher
# Register your models  here.


class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name','created_at']


admin.site.register(Student,StudentAdmin)



class TeacherAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name','created_at']


admin.site.register(Teacher,TeacherAdmin)