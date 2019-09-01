# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics
from . import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets


from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator


class ListProyecto(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer



class DetailProyecto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class ListEmpresa(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer



class DetailEmpresa(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ListDiseno(generics.ListCreateAPIView):
    queryset = Diseno.objects.all()
    serializer_class = DisenoSerializer



class DetailDiseno(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diseno.objects.all()
    serializer_class = DisenoSerializer



@csrf_exempt
def get_data(request):
	data = Proyecto.objects.all()
	if request.method == 'GET':
		serializer = ProyectoSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)