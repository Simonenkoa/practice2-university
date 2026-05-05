from django import forms
from .models import Teacher, Course, Student, TeacherInfo


class TeacherForm(forms.ModelForm) :
    # Поля из TeacherInfo
    phone = forms.CharField(max_length=20, required=False, label="Телефон")
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows' : 4}), required=False, label="Биография")
    diploma = forms.CharField(max_length=200, required=False, label="Диплом / Учёная степень")
    experience_years = forms.IntegerField(required=False, label="Опыт работы (лет)")

    class Meta :
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'department']

    def save(self, commit=True) :
        teacher = super().save(commit=commit)

        # Создаём или обновляем TeacherInfo
        TeacherInfo.objects.update_or_create(
            teacher=teacher,
            defaults={
                'phone' : self.cleaned_data.get('phone', ''),
                'bio' : self.cleaned_data.get('bio', ''),
                'diploma' : self.cleaned_data.get('diploma', ''),
                'experience_years' : self.cleaned_data.get('experience_years') or 0,
            }
        )
        return teacher

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
