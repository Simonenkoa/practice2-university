from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="Email")
    department = models.CharField(max_length=100, blank=True, verbose_name="Кафедра")
    hire_date = models.DateField(null=True, blank=True, verbose_name="Дата найма")

    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    phone = models.CharField(max_length=20, unique=True, blank=True, verbose_name="Телефон")  # уникальный
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Зарплата")
    degree = models.CharField(max_length=100, blank=True, verbose_name="Учёная степень")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class TeacherInfo(models.Model):
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        related_name='info',
        primary_key=True,
        verbose_name="Преподаватель"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    bio = models.TextField(blank=True, verbose_name="Биография")
    diploma = models.CharField(max_length=200, blank=True, verbose_name="Диплом")
    experience_years = models.PositiveIntegerField(default=0, verbose_name="Опыт работы (лет)")
    address = models.TextField(blank=True, verbose_name="Адрес")

    def __str__(self):
        return f"Инфо о {self.teacher}"

    class Meta:
        verbose_name = "Информация о преподавателе"
        verbose_name_plural = "Информация о преподавателях"


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название курса")
    code = models.CharField(max_length=20, unique=True, verbose_name="Код курса")
    description = models.TextField(blank=True, verbose_name="Описание")
    credits = models.PositiveIntegerField(default=3, verbose_name="Кредиты")
    start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала")
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses',
        verbose_name="Преподаватель"
    )
    max_students = models.PositiveIntegerField(default=30, verbose_name="Макс. студентов")

    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    is_active = models.BooleanField(default=True, verbose_name="Активный курс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    student_id = models.CharField(max_length=20, unique=True, verbose_name="Номер студента")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    enrollment_year = models.PositiveIntegerField(verbose_name="Год поступления")
    courses = models.ManyToManyField(
        Course,
        related_name='students',
        blank=True,
        verbose_name="Курсы"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"