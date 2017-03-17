from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

#from django.core.validators import validate_email

from .forms import IscricaoForm

def index(request):
	error = ''

	if request.method == "POST":
		form = IscricaoForm(request.POST)
		if form.is_valid():
			try:
				# verificar telefones
				if len(request.POST.get("telefone") + request.POST.get("telefone")) < 14:
					error = 'Insira um telefone fixo ou celular valido.'
					1/0

				# verificar e-mail
				#validate_email(request.POST.get("email"))

				inscricao = form.save(commit=False)
				inscricao.data_cadastro = timezone.now()
				inscricao.save()
				messages.success(request, 'Pre inscricao realizada com sucesso.')
				form = IscricaoForm()
			except Exception as e:
				if error != '':
					messages.success(request, error)
				else:
					messages.success(request, e.message)
	else:
		form = IscricaoForm()

	return render(request, 'ejc/inscricao.html', {'form': form})