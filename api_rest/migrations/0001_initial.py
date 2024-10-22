# Generated by Django 5.1.2 on 2024-10-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato_nome', models.CharField(default='', max_length=150)),
                ('candidato_nascimento', models.DateField(verbose_name='')),
                ('candidato_cpf', models.IntegerField(default=0)),
                ('candidato_email', models.EmailField(default=0, max_length=254)),
                ('candidato_telefone', models.IntegerField(default=0)),
                ('candidato_endereco', models.CharField(default='', max_length=150)),
                ('candidato_cargo', models.CharField(default='', max_length=150)),
                ('candidato_empresa', models.CharField(default='', max_length=150)),
                ('candidato_descricao', models.CharField(default='', max_length=350)),
                ('candidato_instituicao', models.CharField(default='', max_length=150)),
                ('candidato_curso', models.CharField(default='', max_length=150)),
                ('candidato_periodo', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
