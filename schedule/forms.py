from django import forms
from .models import Teacher, Course, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'department']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'teacher', 'credits']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'student_id']

class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['courses']
        widgets = {
            'courses': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }

class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['courses']
        widgets = {
            'courses': forms.CheckboxSelectMultiple()
        }