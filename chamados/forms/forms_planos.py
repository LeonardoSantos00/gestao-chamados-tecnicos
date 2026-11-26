from django import forms
from chamados.models import Plano


class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'velocidade_download', 'velocidade_upload', 'preco_mensal', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Plano'}),
            'velocidade_download': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'placeholder': 'Velocidade de Download'}),
            'velocidade_upload': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'placeholder': 'Velocidade de Upload'}),
            'preco_mensal': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Preço Mensal'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }