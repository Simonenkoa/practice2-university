from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect   # ← добавили эту строку

# Функция, которая сразу перенаправляет на админку
def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_admin),        # ← эта строка делает главное
]