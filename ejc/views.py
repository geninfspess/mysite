from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import generic

from .forms import InscricaoForm
from .models import Inscricao

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
def InscricaoList(request):
	all_list = Inscricao.objects.order_by('data_cadastro')
	return render(request, 'ejc/inscricao_list.html', {'all_list': all_list})

@login_required
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