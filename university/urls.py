from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from schedule.views import teacher_list, add_teacher, course_list, add_course

def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_admin),                    # главная → админка (как было до 3 лабы)
    path('teachers/', teacher_list, name='teacher_list'),
    path('courses/', course_list, name='course_list'),
    path('add-teacher/', add_teacher, name='add_teacher'),
    path('add-course/', add_course, name='add_course'),
]