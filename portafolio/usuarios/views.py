from django.shortcuts import render, get_object_or_404
# Agregamos las librerias necesarias para trabajar con vistas basadas en clases:
from django.views.generic.base import TemaplateView
# Agregamos la libreria para importar ListViews:
from django.views.generic.list import ListView
# Importamos nuestros modelos:
from .models import Usuarios, Experiencia, Logros, Habilidades, Educacion

# Create your views here.
