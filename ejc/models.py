from django.db import models
from django.utils import timezone

class Comunidade(models.Model):
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Inscricao(models.Model):
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	telefone = models.CharField(max_length=14)
	celular = models.CharField(max_length=15)
	email = models.EmailField(max_length=70, blank=True)
	data_cadastro = models.DateTimeField(default=timezone.now)
	comunidade = models.ForeignKey(Comunidade, null=True, blank=True, default = None)
	ds_comunidade = models.CharField(max_length=200, null=True, blank=True, default = None)
	nome_padrinho = models.CharField(max_length=200, null=True, blank=True)
	telefone_padrinho = models.CharField(max_length=15, null=True, blank=True)
	#nome_padrinho = models.CharField(max_length=200, null=True, blank=True, default = None)
	#telefone_padrinho = models.CharField(max_length=9)
	#celular_padrinho = models.CharField(max_length=10)

	def __str__(self):
		return self.nome