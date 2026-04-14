from django import forms
from django.core.exceptions import ValidationError
from .models import Teacher

# Кастомные валидаторы (3 штуки)
def validate_name_length(value):
    if len(value) < 2:
        raise ValidationError("Имя/фамилия должна быть минимум 2 символа")

def validate_phone(value):
    if value and not value.startswith('+7'):
        raise ValidationError("Телефон должен начинаться с +7")

def validate_salary(value):
    if value and value < 10000:
        raise ValidationError("Зарплата не может быть меньше 10000")

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'department', 'birth_date', 'phone', 'salary']

    # 3 метода clean_ для полей
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        validate_name_length(data)
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        validate_name_length(data)
        return data

    def clean_phone(self):
        data = self.cleaned_data.get('phone')
        if data:
            validate_phone(data)
        return data

    # 2 метода clean() для формы
    def clean(self):
        cleaned_data = super().clean()
        salary = cleaned_data.get('salary')
        if salary:
            validate_salary(salary)
        return cleaned_data

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary and salary > 500000:
            raise ValidationError("Зарплата не может быть больше 500000")
        return salary