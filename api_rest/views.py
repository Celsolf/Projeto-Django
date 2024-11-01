from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Candidato
from .forms import CandidatoForm
from .serializers import CandidatoSerializer

import json


@login_required
@api_view(['GET'])
def get_candidatos(request):

    if request.method == 'GET':

        candidatos = Candidato.objects.all()
        serializer = CandidatoSerializer(candidatos, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def get_by_cpf(request,cpf):

    try:
        candidato = Candidato.objects.get(candidato_cpf = cpf)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':

        serializer=CandidatoSerializer(candidato)
        return Response(serializer.data)
    

@login_required
def inserir_candidato(request):
    if request.method == "POST":
        form = CandidatoForm(request.POST)
        if form.is_valid():
               form.save()
               messages.success(request, "candidato adicionado")
               return redirect('inserir_candidato')
        else:
            messages.error(request, "Erro no formulário. Por favor, verifique os campos.Os campos de cpf,email ou telefone já estão registrados.")
        
    else:
        form = CandidatoForm()
    return render(request, 'inserir_candidato.html', {'form': form})


def excluir_candidato(request, id):
    candidato =Candidato.objects.get(id=id)
    if request.method == "POST":
        candidato.delete()
        return redirect('get_candidatos')
    return render(request, 'excluir_candidato.html', {'candidato': candidato})



@api_view(['PUT','DELETE'])
def candidato_manager(request):

#edição

    if request.method =="PUT":

        cpf= request.data['candidato_cpf']
        try:
            update_candidato = Candidato.objects.get(candidato_cpf=cpf)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CandidatoSerializer(update_candidato,data =request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #deletar

    if request.method =="DELETE":

        try:
            candidato_to_delete = Candidato.objects.get(candidato_cpf=request.data["candidato_cpf"])
            candidato_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Candidato.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)