from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.forms import CursoFormulario, ProfesorFormulario

from .models import Curso, Profesor

def crear_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()

    return HttpResponse(f"Curso creado! {camada}")


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = CursoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            
            curso.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = CursoFormulario()
    
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def profesorFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = ProfesorFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            profesor = Profesor( nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            
            profesor.save()
            
            return render(request, "AppCoder/inicio.html")
    
    else:
        miFormulario = ProfesorFormulario()
        
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscarCamada(request):
    
    if request.GET["camada"]:
        
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
    
    else:
        respuesta= "No enviaste datos"

    
    return HttpResponse(respuesta)