from django.db import models
from django.utils import timezone

class Comunidade(models.Model):
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Inscricao(models.Model):
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	telefone = models.CharField(max_length=14, null=True, blank=True)
	celular = models.CharField(max_length=15, null=True, blank=True)
	email = models.EmailField(max_length=70, null=True, blank=True)
	data_cadastro = models.DateTimeField(default=timezone.now)
	comunidade = models.ForeignKey(Comunidade, null=True, blank=True, default = None)
	ds_comunidade = models.CharField(max_length=200, null=True, blank=True, default = None)
	nome_padrinho = models.CharField(max_length=200, null=True, blank=True)
	telefone_padrinho = models.CharField(max_length=15, null=True, blank=True)
	endereco = models.CharField(max_length=200, default='')
	usuario_alteracao = models.ForeignKey('auth.User', blank=True, null=True)
	data_alteracao = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.nome

class Encontro(models.Model):
	descricao = models.CharField(max_length=200)
	data = models.DateField()
	logo = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.descricao

class Equipe(models.Model):
	nome = models.CharField(max_length=200)
	logo = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.nome

class Servo(models.Model):
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	email = models.EmailField(max_length=70, null=True, blank=True)
	email2 = models.EmailField(max_length=70, null=True, blank=True)
	telefone = models.CharField(max_length=14, null=True, blank=True)
	celular = models.CharField(max_length=15, null=True, blank=True)
	celular2 = models.CharField(max_length=15, null=True, blank=True)
	comunidade = models.ForeignKey(Comunidade, null=True, blank=True, default = None)
	outra_comunidade = models.CharField(max_length=200, null=True, blank=True, default = None)
	equipe = models.ForeignKey(Equipe)
	usuario_alteracao = models.ForeignKey('auth.User', blank=True, null=True)
	data_alteracao = models.DateTimeField(null=True, blank=True)
	coordenador = models.BooleanField(default=False)

	def __str__(self):
		return self.nome

class Coordenador(models.Model):
	equipe = models.ForeignKey(Equipe)
	usuario = models.ForeignKey('auth.User')

	def __str__(self):
		return self.usuario.username