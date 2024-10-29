from django import forms
from .models import Candidato

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato  
        fields = ['candidato_nome', 'candidato_nascimento', 'candidato_cpf', 'candidato_email',
                  'candidato_telefone', 'candidato_endereco', 'candidato_cargo', 'candidato_empresa', 
                  'candidato_periodo', 'candidato_descricao', 'candidato_instituicao', 'candidato_curso', 
                  'candidato_periodo'] 
