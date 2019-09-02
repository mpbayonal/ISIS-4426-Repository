# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics
from . import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly




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


class ListDiseno(generics.ListCreateAPIView):
    queryset = Diseno.objects.all()
    serializer_class = DisenoSerializer




class DetailDiseno(generics.RetrieveUpdateDestroyAPIView):
	queryset = Diseno.objects.all()
	serializer_class = DisenoSerializer
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = (IsAuthenticatedOrReadOnly,)





@csrf_exempt
def get_data(request):
	data = Proyecto.objects.all()
	if request.method == 'GET':
		serializer = ProyectoSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)