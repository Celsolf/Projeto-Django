from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Candidato
from .forms import CandidatoForm
from .serializers import CandidatoSerializer

import json

#testes
@api_view(['GET'])
def get_candidatos(request):

    if request.method == 'GET':

        candidatos = Candidato.objects.all()
        serializer = CandidatoSerializer(candidatos, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_cpf(request,cpf):

    try:
        candidato = Candidato.objects.get(pk = cpf)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':

        serializer=CandidatoSerializer(candidato)
        return Response(serializer.data)
    

def inserir_candidato(request):
    if request.method == "POST":
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_candidatos')  # Redireciona após o cadastro
    else:
        form = CandidatoForm()
    return render(request, 'inserir_candidato.html', {'form': form})

# views.py
def excluir_candidato(request, id):
    candidato =Candidato.objects.get(id=id)
    if request.method == "POST":
        candidato.delete()
        return redirect('get_candidatos')
    return render(request, 'excluir_candidato.html', {'candidato': candidato})


# CRUD
@api_view(['GET','POST','PUT','DELETE'])
def candidato_manager(request):

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['candidato']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                candidato_cpf = request.GET['candidato']         # Find get parameter

                try:
                    candidato = Candidato.objects.get(pk=candidato_cpf)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = CandidatoSerializer(candidato)           # Serialize the object data into json
                return Response(serializer.data)                        # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#criação
    if request.method =="POST":

        new_candidato= request.data
        serializer = CandidatoSerializer(data = new_candidato)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

#edição

    if request.method =="PUT":

        cpf= request.data['candidato_cpf']
        try:
            update_candidato = Candidato.objects.get(pk=cpf)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CandidatoSerializer(update_candidato,data =request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    