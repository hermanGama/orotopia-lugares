"""orotopia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('login', acceder, name='login'),

	path('iniciar', iniciar_sesion, name='iniciar'),
	path('<int:id>/vermas', vermas, name='vermas'),
	path('', vistasPage, name='vistasPage'),
	path('logout', cerrar_sesion, name='url_logout'),
	path('base',base, name='base'),
	path('<int:id>/ver/', detalleVista, name='detalleVista'),
	path('<int:id>/eliminar/', eliminarVista, name='eliminarVista'),
	path('agregar/vistas', agregarVistas, name='agregarVistas'),
	path('template',listarTemplate, name='listarTemplate'),
	path('vistas',listarVistas, name='listarVistas'),
	path('<int:id>/edit/vista',editVista, name='editVista'),
	path('<int:id>/edit/contenido',editContenido, name='editContenido'),
	path('<int:id>/edit/template',editTemplate, name='editTemplate'),
	path('<int:id>/add/contenido', agregarContenido, name='agregarContenido'),
	path('<int:id>/listar/contenido', listarContenido, name='listarContenido'),
	path('vcontenido', listarVistasContenido, name='listarVistasContenido'),

]
