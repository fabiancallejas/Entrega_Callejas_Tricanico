import email
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from AppCoder.models import Curso,Profesor,Estudiante,Entregable
from django.template import loader
from AppCoder.forms import CursoFormulario,ProfesorFormulario,EstudianteFormulario,EntregableFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

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
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render (request, 'appCoder/resultadoBusqueda.html', {'cursos':cursos, 'camada':camada})
    else:
     respuesta = f"No se han encontrado resultados"
    return HttpResponse(respuesta)

def busquedaProfesor(request):
 return render(request, 'appCoder/busquedaProfesor.html')

def buscarProfesor(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        apellido = Profesor.objects.filter(nombre=nombre)
        return render (request, 'appCoder/resultadoBusquedaProfesor.html', {'nombre':nombre, 'apellido':apellido})
    else:
     respuesta = f"No se han encontrado resultados"
    return HttpResponse(respuesta)

#CRUD Read - Profesor
def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}    
    return render (request, 'appCoder/profesores.html', contexto)

#CRUD Create - Profesor
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

#CRUD Delete - Profesor
def eliminarProfesor (request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}
    return render (request, "appCoder/profesores.html", contexto)

#CRUD Update - Profesor
def editarProfesor (request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion ['nombre']
            profesor.apellido = informacion ['apellido']
            profesor.email = informacion ['email']
            profesor.profesion = informacion ['profesion']
            profesor.save() 

            profesores = Profesor.objects.all()
            contexto = {'profesores':profesores}
            return render (request, "appCoder/profesores.html", contexto)
    else:
        miFormulario = ProfesorFormulario(initial= {'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email ,'profesion': profesor.profesion})
        contexto = {'miFormulario':miFormulario,'nombre':nombre}
        return render(request, 'appCoder/editarProfesor.html' , contexto)


##ListView

class EstudiantesList(LoginRequiredMixin,ListView):
    model = Estudiante
    template_name = 'appCoder/estudiante_list.html'

#DetailView
class EstudianteDetalle(DetailView):
    model = Estudiante
    template_name = 'appCoder/estudiante_detalle.html'

#CreateView
class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido', 'email']

#UpdateView
class EstudianteEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido', 'email']

#DeleteView
class EstudianteEliminar(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')


##Login
def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      clave = form.cleaned_data.get('password')
      # Autenticación de usuario
      user = authenticate(username=usuario, password=clave) # Si este usuario existe me lo trae
      if user is not None:
        login(request,user) # Si existe, lo loguea
        return render(request, 'AppCoder/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
      else:
        return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, datos incorrectos'})
    else:
      return render(request,'AppCoder/inicio.html', {'mensaje': 'Error, formulario erróneo'})
  form = AuthenticationForm() # Creo un formulario vacío si vengo por GET
  return render(request, 'AppCoder/login.html', {'form':form}) 

# REGISTER
def register_request(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return render(request, 'AppCoder/inicio.html', {'mensaje': f'Usuario {username} creado'})
    else:
      return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})
  else:
    form = UserRegistrationForm()
    return render(request, 'AppCoder/register.html', {'form':form})