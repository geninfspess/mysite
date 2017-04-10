from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.decorators import permission_required

from .forms import InscricaoForm
from .forms import ServoForm

from .models import Inscricao
from .models import Equipe
from .models import Servo
from .models import Coordenador

def index(request):
	error = ''

	if request.method == "POST":

		if request.POST.get("emensagem"):
			mensagem = 'From: ' + request.POST['eemail'] + '\n\n' + request.POST['emensagem'];
			send_mail(request.POST['eassunto'], mensagem, request.POST['eemail'], ['ejcpnsgloria@gmail.com'], fail_silently=False)
			messages.success(request, 'E-mail enviado com sucesso.')

		form = InscricaoForm(request.POST)
		if form.is_valid():
			try:
				# verificar telefones
				if len(request.POST.get("telefone") + request.POST.get("celular")) < 14:
					error = 'Insira um telefone fixo ou celular valido.'
					1/0

				# verificar e-mail
				#validate_email(request.POST.get("email"))

				inscricao = form.save(commit=False)
				inscricao.data_cadastro = timezone.now()
				inscricao.save()
				messages.success(request, 'Pre inscricao realizada com sucesso.')
				form = InscricaoForm()
			except Exception as e:
				if error != '':
					messages.success(request, error)
				else:
					messages.success(request, e.message)
	else:
		form = InscricaoForm()

	return render(request, 'ejc/inscricao_view.html', {'form': form})

@login_required
@permission_required('ejc.add_inscricao')
def InscricaoList(request):
	permission_required = 'global_permissions.pode_acessar_pagina_config'

	all_list = Inscricao.objects.order_by('data_cadastro')
	return render(request, 'ejc/inscricao_list.html', {'all_list': all_list})

@login_required
@permission_required('ejc.change_inscricao')
def InscricaoEdit(request, pk):
    inscricao = get_object_or_404(Inscricao, pk=pk)

    if request.method == "POST":
        form = InscricaoForm(request.POST, instance=inscricao)
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.usuario_alteracao = request.user
            inscricao.data_alteracao = timezone.now()
            inscricao.save()
            messages.success(request, 'Inscricao alterada com sucesso.')
            return InscricaoList(request)
    else:
        form = InscricaoForm(instance=inscricao)
        return render(request, 'ejc/inscricao_edit.html', {'form': form})

@login_required
@permission_required('ejc.add_servo')
def ServoList(request):
	id_user = request.user.id
	coord = Coordenador.objects.filter(usuario=id_user)

	if coord:
		coord_list = Servo.objects.filter(equipe=coord[0].equipe, coordenador=True).order_by('nome')
		servo_list = Servo.objects.filter(equipe=coord[0].equipe, coordenador=False).order_by('nome')
		equipe = coord[0].equipe.nome
	else:
		coord_list = []
		servo_list = []
		equipe = ''

	return render(request, 'ejc/servo_list.html', {'coord_list': coord_list, 'servo_list': servo_list, 'equipe': equipe})

@login_required
@permission_required('ejc.change_servo')
def ServoEdit(request, pk):
    servo = get_object_or_404(Servo, pk=pk)

    if request.method == "POST":
        form = ServoForm(request.POST, instance=servo)
        if form.is_valid():
            servo = form.save(commit=False)

            if request.POST.get("hdExcluir") == 'true':
            	servo.delete()
            else:
            	servo.usuario_alteracao = request.user
            	servo.data_alteracao = timezone.now()
            	servo.save()

            messages.success(request, 'Servo alterado com sucesso.')
            return ServoList(request)	
    else:
        form = ServoForm(instance=servo)

    return render(request, 'ejc/servo_edit.html', {'form': form, 'title': 'Alterar Servo'})

@login_required
@permission_required('ejc.add_servo')
def ServoNew(request):
	if request.method == "POST":
		form = ServoForm(request.POST)
		if form.is_valid():
			id_user = request.user.id
			coord = Coordenador.objects.filter(usuario=id_user)
			servo = form.save(commit=False)
			servo.equipe = coord[0].equipe
			servo.save()
			messages.success(request, 'Servo salvo com sucesso.')
			form = ServoForm()
	else:
		form = ServoForm()
	
	return render(request, 'ejc/servo_edit.html', {'form': form, 'title': 'Adicionar Servo'})