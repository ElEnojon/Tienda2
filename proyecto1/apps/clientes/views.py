from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from apps.clientes.models import Cliente
from apps.clientes.forms import ClienteForm


def index(request):
	return HttpResponse("Esta es la respuesta");

def plantilla(request):
	return render(request, 'clientes/index.html');

# def especial(request):
# 	return render(request,'clientes/paginaespecial.html');


def especial(request):
	contexto = {
		'clientes':Cliente.objects.all()
	} 
	return render(request, 'clientes/paginaespecial.html', contexto)

def nuevoRegistro(request):
	form = ClienteForm()
	return render(request, 'clientes/clienteformulario.html',{'form' :form})

def editarRegistro(request, idCliente):
	cliente = Cliente.objects.get(id=idCliente)
	if(request.method == 'GET'):
		form = ClienteForm(instance=cliente)
	else: 
		form= ClienteForm(request.POST, instance=cliente)

	if form.is_valid():
		form.save()
		return redirect('clientes:listaClientes')
		return render(request, 'clientes/clienteformulario.html',{'form' :form})

		
class viewClientes(ListView):
	model= Cliente
	# queryset = Cliente.objects.filter(nombre='roberto') esta linea solo muestra los robertos
	template_name = 'clientes/paginaespecial.html'




