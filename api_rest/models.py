from django.db import models

class Candidato(models.Model):
    candidato_nome = models.CharField(max_length=150, default='')
    candidato_nascimento =models.DateField((""), auto_now=False, auto_now_add=False)
    candidato_cpf =models.IntegerField(primary_key= True, default=0)

    candidato_email =models.EmailField(default=0)
    candidato_telefone =models.IntegerField(default=0)
    candidato_endereco =models.CharField(max_length=150, default='')
    candidato_cargo =models.CharField(max_length=150, default='')
    candidato_empresa =models.CharField(max_length=150, default='')
    candidato_periodo =models.CharField(max_length=150, default='')

    candidato_descricao =models.CharField(max_length=350, default='')
    candidato_instituicao =models.CharField(max_length=150, default='')
    candidato_curso =models.CharField(max_length=150, default='')
    candidato_periodo =models.CharField(max_length=150, default='')

    def __str__(self):
        return f'Nome: {self.candidato_nome} | E-mail:{self.candidato_email}'

