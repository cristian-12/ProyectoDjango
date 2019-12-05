# importamos la libreria forms
from django import forms
# Creamos una lista de posibles peticiones del select
from .pqrsf import PQRSF_CHOICES

# Creamos la estructura del formulario:
class ContactForm(forms.Form):
	"""docstring for ContactForm"""
	email = forms.EmailField(label="correo Electronico", widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
	tipom = forms.ChoiceField(choices = PQRSF_CHOICES, label="Tipo de atencion requerida", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True)
	nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	msj = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}), required=True)
