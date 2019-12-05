from django.db import models
from ckeditor.fields import RichTextField

# Create your models here. importamos la lista de tipos de mensajes
from .pqrsf import PQRSF_CHOICES

# Create your models here

class Contact(models.Model):
	"""docstring for Contact"""
	email = models.EmailField(max_length = 50, verbose_name = "Correo electronico")
	tipom = models.CharField(max_length = 50, choices=PQRSF_CHOICES, default="Peticion", verbose_name = "Categoria")
	nombre = models.CharField(max_length = 250, verbose_name = "Nombre")
	msj = RichTextField(default="Quisiera", verbose_name = "Mensaje")

	class Meta:
		verbose_name = "Mensajes PQRSF"
		verbose_name_plural = "Mensajes PQRSF"

	def __str__(self):
		return self.nombre
