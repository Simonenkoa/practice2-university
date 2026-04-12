from django import forms

class TeacherForm(forms.Form):
    first_name = forms.CharField(
        label="Имя",
        help_text="Введите имя преподавателя",
        widget=forms.TextInput(attrs={'placeholder': 'Иван'})
    )
    last_name = forms.CharField(
        label="Фамилия",
        help_text="Введите фамилию преподавателя",
        widget=forms.TextInput(attrs={'placeholder': 'Иванов'})
    )
    email = forms.EmailField(
        label="Email",
        help_text="Введите рабочий email",
        widget=forms.EmailInput(attrs={'placeholder': 'ivanov@university.ru'})
    )
    department = forms.CharField(          # это поле сделаем необязательным
        label="Кафедра",
        required=False,
        help_text="Кафедра (необязательно)",
        widget=forms.TextInput(attrs={'placeholder': 'Информатика'})
    )

class CourseForm(forms.Form):
    name = forms.CharField(
        label="Название курса",
        help_text="Введите полное название курса",
        widget=forms.TextInput(attrs={'placeholder': 'Python для начинающих'})
    )
    code = forms.CharField(
        label="Код курса",
        help_text="Уникальный код (например PY101)",
        widget=forms.TextInput(attrs={'placeholder': 'PY101'})
    )
    description = forms.CharField(
        label="Описание",
        required=False,                    # необязательное поле
        widget=forms.Textarea(attrs={'placeholder': 'Краткое описание курса...', 'rows': 3})
    )
    credits = forms.IntegerField(
        label="Кредиты",
        initial=3,
        help_text="Количество кредитов",
        widget=forms.NumberInput(attrs={'placeholder': '3'})
    )