import email
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso,Profesor,Estudiante,Entregable
from django.template import loader
from AppCoder.forms import CursoFormulario,ProfesorFormulario,EstudianteFormulario,EntregableFormulario


# Create your views here.
def curso (self):
    curso = Curso (nombre="Desarrollo Web", camada=16740 )
    curso.save()
    documento = f"Curso: {curso.nombre} - Camada {curso.camada}"
    return HttpResponse(documento)

def profesores (request):
    documento = f"Pagina de Profesores"
    return render(request, 'appCoder/profesores.html')

def cursos (self):
    documento = f"Pagina de Cursos"
    return HttpResponse(documento)

def estudiantes (self):
    documento = f"Pagina de Estudiantes"
    return HttpResponse(documento)

def entregables (self):
    documento = f"Pagina de Entregables"
    return HttpResponse(documento)

def inicio(self):
    plantilla =loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['curso']
        camada = informacion ['camada']
        curso = Curso(nombre=nombre, camada=camada) 
        curso.save() 
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()
    return render(request, 'appCoder/cursoFormulario.html' , {'miFormulario':miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        apellido = informacion ['apellido']
        email = informacion ['email']
        profesion = informacion ['profesion']
        profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion) 
        profesor.save() 
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()
    return render(request, 'appCoder/profesorFormulario.html' , {'miFormulario':miFormulario})

def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        apellido = informacion ['apellido']
        email = informacion ['email']
        estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email) 
        estudiante.save() 
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = EstudianteFormulario()
    return render(request, 'appCoder/estudianteFormulario.html' , {'miFormulario':miFormulario})

def entregableFormulario(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        fechaDeEntrega = informacion ['fechaDeEntrega']
        entregado = informacion ['entregado']
        entrega = Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entregado=entregado) 
        entrega.save() 
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = EntregableFormulario()
    return render(request, 'appCoder/entregableFormulario.html' , {'miFormulario':miFormulario})

def busquedaCamada(request):
 return render(request, 'appCoder/busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        camada =  request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render (request, 'appCoder/resultadoBusqueda.html', {'cursos':cursos, 'camada':camada})
    else:
     respuesta = f"No se han encontrado resultados"
    return HttpResponse(respuesta)

def busquedaProfesor(request):
 return render(request, 'appCoder/busquedaProfesor.html')

def buscarProfesor(request):
    if request.GET['nombre']:
        print(request.GET)
        nombre =  request.GET['nombre']
        print(nombre)
        profesor = Profesor.objects.filter(nombre=nombre)
        return render (request, 'appCoder/resultadoBusquedaProfesor.html', {'nombre':nombre},)
    else:
     respuesta = f"No se han encontrado resultados"
    return HttpResponse(respuesta)