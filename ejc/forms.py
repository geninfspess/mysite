from django import forms
from .models import Inscricao, Comunidade, Servo

class InscricaoForm(forms.ModelForm):

    class Meta:
        model = Inscricao
        fields = ('nome', 'data_nascimento', 'endereco', 'telefone', 'celular', 'email', 'comunidade', 'ds_comunidade', 
        	'nome_padrinho', 'telefone_padrinho')
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'class':'datepicker'}),
            'nome': forms.DateInput(attrs={'class':'tx_big'}),
            'endereco': forms.DateInput(attrs={'class':'tx_big'}),
            'email': forms.DateInput(attrs={'class':'tx_big'}),
            'ds_comunidade': forms.DateInput(attrs={'class':'tx_big'}),
            'nome_padrinho': forms.DateInput(attrs={'class':'tx_big'}),
        }

class ServoForm(forms.ModelForm):

    class Meta:
        model = Servo
        fields = ('nome', 'data_nascimento', 'email', 'email2', 'telefone', 'celular', 'celular2', 'comunidade', 'outra_comunidade', 'coordenador')
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'class':'datepicker'}),
            'nome': forms.DateInput(attrs={'class':'tx_big'}),
            'email': forms.DateInput(attrs={'class':'tx_big'}),
            'email2': forms.DateInput(attrs={'class':'tx_big'}),
            'outra_comunidade': forms.DateInput(attrs={'class':'tx_big'}),
        }