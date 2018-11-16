from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	fechaHBD = models.DateField(default ='2000-01-01')
	numHijos = models.IntegerField(default = 0)

class Pedido(models.Model):
	cliente = models.ForeignKey(Cliente, null=True, blank = True, on_delete = models.CASCADE)
		