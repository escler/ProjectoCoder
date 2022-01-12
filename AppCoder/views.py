from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

def crear_curso(request, camada):
    curso = Curso(nombre='Python', camada=camada)
    curso.save()
    
    return HttpResponse(f'Curso {curso.nombre} Creado! Camada: {camada}')

def inicio(request):
    HttpResponse('inicio')

def cursos(request):
    HttpResponse('cursos')
    
def profesores(request):
    HttpResponse('profesores')
    
def estudiantes(request):
    HttpResponse('estudiantes')

def entregables(request):
    HttpResponse('entregables')