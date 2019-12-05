from django.shortcuts import render, redirect
from django.http import HttpResponse
#cargamos el formulario
from .forms import ContactForm

# Create your views here. creamos nuestra vista de index


def indexcore(request):
	# Instaciamos el formulario de contacto
	FormContact = ContactForm()
	# Validamos que se haya hecho la peticion post del formulario de contacto
	if request.method == "POST":
		# Reasignamos el valor de formcontact
		if FormContact.is_valid():
			# Retornamos los valores de los campos:
			email = request.POST.get('email', '')
			tipom = request.POST.get('tipom', '')
			nombre = request.POST.get('nombre', '')
			msj = request.POST.get('msj', '')
			# si todo sale bien, guardamos y redireccionamos al nombre de la url
			FormContact.save()
			return redirect(reserve('inicio')+"?0k")
	return render(request,'core/index.html', {'formulario': FormContact} )

def perfil(request):
	return render(request,'core/hv.html' )