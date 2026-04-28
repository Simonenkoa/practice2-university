from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Teacher, Course, Student
from .forms import TeacherForm, CourseForm, StudentForm, StudentCourseForm

# ====================== TEACHER ======================
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'schedule/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'schedule/teacher_form.html', {'form': form, 'title': 'Добавить преподавателя'})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'schedule/teacher_form.html', {'form': form, 'title': 'Редактировать преподавателя'})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'schedule/teacher_confirm_delete.html', {'object': teacher, 'type': 'преподавателя'})

# ====================== COURSE ======================
def course_list(request):
    teachers = Teacher.objects.all()
    selected_teacher = request.GET.get('teacher')
    courses = Course.objects.all()
    if selected_teacher:
        courses = courses.filter(teacher_id=selected_teacher)
    return render(request, 'schedule/course_list.html', {
        'courses': courses,
        'teachers': teachers,
        'selected_teacher': selected_teacher
    })

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'schedule/course_form.html', {'form': form, 'title': 'Добавить курс'})

# ====================== STUDENT ======================
def student_list(request):
    students = Student.objects.all()
    return render(request, 'schedule/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'schedule/student_form.html', {'form': form, 'title': 'Добавить студента'})

# ====================== ORM ЗАПРОСЫ ======================
def orm_page(request):
    query = request.GET.get('query')
    context = {
        'query': query,
    }

    if query == 'teachers_many':
        context['teachers_many'] = Teacher.objects.annotate(course_count=Count('courses')).filter(course_count__gt=1)
    elif query == 'students_no_courses':
        context['students_no_courses'] = Student.objects.filter(courses__isnull=True)
    elif query == 'teachers_no_info':
        context['teachers_no_info'] = Teacher.objects.filter(info__isnull=True)

    return render(request, 'schedule/orm.html', context)

# ====================== STUDENT + КУРСЫ ======================
def student_update_courses(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentCourseForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentCourseForm(instance=student)
    return render(request, 'schedule/student_courses_form.html', {
        'form': form,
        'student': student,
        'title': f'Запись студента {student} на курсы'
    })

# ====================== TEACHER INFO ======================
def teacher_info(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    try:
        info = teacher.info
    except TeacherInfo.DoesNotExist:
        info = None
    return render(request, 'schedule/teacher_info.html', {
        'teacher': teacher,
        'info': info
    })