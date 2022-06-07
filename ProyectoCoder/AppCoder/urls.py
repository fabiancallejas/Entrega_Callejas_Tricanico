from django.urls import path
from AppCoder.views import profesores, curso, inicio, entregables, estudiantes, cursos, cursoFormulario, profesorFormulario,estudianteFormulario,entregableFormulario,busquedaCamada,buscar,busquedaProfesor,buscarProfesor


urlpatterns = [
    path('curso/', curso, ),
    path('profesores/', profesores, name='Profesores'),
    path('entregables/', entregables, name='Entregables'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('cursos/', cursos, name='Cursos'),
    path('inicio/', inicio, name='Inicio'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
    path('estudianteFormulario/', estudianteFormulario, name='estudianteFormulario'),
    path('entregableFormulario/', entregableFormulario, name='entregableFormulario'),
    path('busquedaCamada/', busquedaCamada, name='busquedaCamada'),
    path('buscar/', buscar, name='buscar'),
    path('busquedaProfesor/', busquedaProfesor, name='busquedaProfesor'),
    path('buscarProfesor/', buscarProfesor, name='buscarProfesor'),

]
