# Generated by Django 5.1.2 on 2024-11-01 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_remove_candidato_id_alter_candidato_candidato_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='candidato_email',
            field=models.EmailField(default=0, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='candidato_telefone',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
