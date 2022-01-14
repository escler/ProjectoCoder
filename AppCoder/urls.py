from django.urls import path

from AppCoder.views import crear_curso, cursos, inicio, profesores, entregables, estudiantes

urlpatterns = [
    path('crear_curso/<camada>', crear_curso),
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='Cursos'),
    path('profesores', profesores, name='Profesores'),
    path('entregables', entregables, name='Entregables'),
    path('estudiantes', estudiantes, name='Estudiantes')
]