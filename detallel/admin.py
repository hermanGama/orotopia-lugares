from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(PrincipalPage)
admin.site.register(imagenVista)
admin.site.register(detalleImagen)

