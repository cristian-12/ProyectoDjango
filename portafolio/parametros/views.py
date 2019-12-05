from django.shortcuts import render

# Create your views here. creamos nuestra vista de index


def indexcore(request):
	return render(request,'core/index.html')

def perfil(request):
	return render(request,'core/hv.html' )
