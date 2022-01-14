from django.contrib import admin

from AppCoder.views import profesores
from .models import *

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
