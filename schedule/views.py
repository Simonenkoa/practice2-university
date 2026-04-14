from django.shortcuts import render, redirect
from .models import Teacher, Course
from .forms import TeacherForm, CourseForm
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'schedule/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()          # ModelForm сам сохраняет в модель
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'schedule/add_teacher.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'schedule/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            Course.objects.create(
                name=form.cleaned_data['name'],
                code=form.cleaned_data['code'],
                description=form.cleaned_data['description'],
                credits=form.cleaned_data['credits']
            )
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'schedule/add_course.html', {'form': form})