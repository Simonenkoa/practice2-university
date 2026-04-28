from django.urls import path
from schedule.views import (
    teacher_list, teacher_create, teacher_update, teacher_delete,
    course_list, course_create,
    student_list, student_create, student_update_courses,
    teacher_info, orm_page
)

urlpatterns = [
    path('', teacher_list, name='home'),                    # Главная — список преподавателей

    # Teacher
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/add/', teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/edit/', teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', teacher_delete, name='teacher_delete'),
    path('teachers/<int:pk>/info/', teacher_info, name='teacher_info'),

    # Course
    path('courses/', course_list, name='course_list'),
    path('courses/add/', course_create, name='course_create'),

    # Student
    path('students/', student_list, name='student_list'),
    path('students/add/', student_create, name='student_create'),
    path('students/<int:pk>/courses/', student_update_courses, name='student_update_courses'),

    # ORM
    path('orm/', orm_page, name='orm_page'),
]