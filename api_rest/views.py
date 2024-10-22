from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Candidato
from .serializers import CandidatoSerializer

import json


@api_view(['GET'])
def get_candidatos(request):

    if request.method == 'GET':

        candidatos = Candidato.objects.all()
        serializer = CandidatoSerializer(candidatos, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)