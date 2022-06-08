from django.urls import path
from AppCoder.views import leerProfesores, eliminarProfesor, profesores, curso, inicio, entregables, estudiantes, cursos, cursoFormulario, profesorFormulario,estudianteFormulario,entregableFormulario,busquedaCamada,buscar,busquedaProfesor,buscarProfesor,editarProfesor,EstudiantesList,EstudianteCreacion,EstudianteEdicion,EstudianteDetalle,EstudianteEliminar


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
    path('leerProfesores/', leerProfesores, name='LeerProfesores'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name='eliminarProfesor'),
    path('editarProfesor/<nombre>', editarProfesor, name='editarProfesor'),

    #####
    path('estudiante/list/', EstudiantesList.as_view(), name='estudiante_list'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/edicion/<pk>', EstudianteEdicion.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteEliminar.as_view(), name='estudiante_eliminar'),





]
