from django.urls import path
from apps.clientes.views import index, plantilla, especial,viewClientes, nuevoRegistro, editarRegistro


app_name= 'clientes'

urlpatterns = [
	path('',index),
    path('index', index),
    path('plantilla',plantilla),
    path('especial', viewClientes.as_view()),
    path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro")
    path('editarRegistro/<idCliente>', editarRegistro, name="editarRegistro")
    ]