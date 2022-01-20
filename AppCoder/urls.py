from django.urls import path

from AppCoder.views import buscarCamada, busquedaCamada, crear_curso, cursos, inicio, profesores, entregables, estudiantes, cursoFormulario, profesorFormulario

urlpatterns = [
    path('crear_curso/<camada>', crear_curso),
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='Cursos'),
    path('profesores', profesores, name='Profesores'),
    path('entregables', entregables, name='Entregables'),
    path('estudiantes', estudiantes, name='Estudiantes'),
    path('cursoFormulario', cursoFormulario, name='CursoFormulario'),
    path('profesorFormulario', profesorFormulario, name='ProfesorFormulario'),
    path('busquedaCamada', busquedaCamada, name='BusquedaCamada'),
    path('buscarCamada/', buscarCamada)
]