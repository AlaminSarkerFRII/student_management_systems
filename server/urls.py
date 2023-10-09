
from django.contrib import admin
from django.urls import path,include
from students.views import index



admin.site.site_header = "Student Management System"
admin.site.site_title = "Student Management System"
admin.site.title_index = "Student Management System"




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home.views.index, name='index'),
    # path('home/', home.views.index, name='index'),
    path('', include('students.urls')),
    # path('students/register/', students.views.register, name='register'),
    # path('students/login/', students.views.login, name='login'),
]
