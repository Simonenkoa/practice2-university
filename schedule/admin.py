from django.contrib import admin
from .models import Teacher, TeacherInfo, Course, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department')

@admin.register(TeacherInfo)
class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'phone', 'experience_years')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'teacher', 'credits')
    list_filter = ('teacher',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'enrollment_year')
    filter_horizontal = ('courses',)