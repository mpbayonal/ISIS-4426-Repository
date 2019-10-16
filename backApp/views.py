import base64
import os
from datetime import datetime

import pytz
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework import generics, permissions, serializers, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view
from rest_framework.permissions import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from ..back.celery import app
from . import serializers
from .models import *
from .serializers import *
from .tasks import process_image_and_send_mail


class ListProyecto(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    # def create(self, request, *args, **kwargs): # don't need to `self.request` since `request` is available as a parameter.
    #     serializer = self.serializer_class(request.data)
    #     data = serializer.data
    #     os.mkdir(data['nombre'])
    #     return JsonResponse(serializer.data, safe=False)


class DetailProyecto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class ListDiseno(generics.ListCreateAPIView):
    queryset = Diseno.objects.all()
    serializer_class = DisenoSerializer


class DetailDiseno(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diseno.objects.all()
    serializer_class = DisenoSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = (IsAuthenticatedOrReadOnly,)


@csrf_exempt
def get_proyectos_Url(request, urlLink):

    if request.method == 'GET':

        user = UserCustom.objects.get(url = urlLink)
        data = Proyecto.objects.filter(empresa_id= user.id)
        serializer = ProyectoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_diseno_proyecto(request, proyecto_id):

    if request.method == 'GET':

        proyecto = Proyecto.objects.get(id = proyecto_id)
        data = Diseno.objects.filter(
            proyecto_id= proyecto.id).filter(
                estado="Disponible")  
        serializer = DisenoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_url_email(request, pUsername):

    if request.method == 'GET':
        user = UserCustom.objects.get(username = pUsername)
        user.url = user.username + "" + str(user.id)
        user.save()
        serializer = UserCustomURLSerializer(user, many=False)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def send_diseno(request):

    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        input_image = files['image']
        proyecto = Proyecto.objects.get(id = data['proyecto'])
        nuevoDiseño = Diseno(
            nombre=data['nombre'],
            apellido=data['apellido'],
            email=data['email'],
            estado=data['estado'],
            pago=data['pago'],
            proyecto=proyecto,
            archivo=input_image
        )
        nuevoDiseño.save()
        app.send_task("send_feedback_email_task", kwargs=dict(id=nuevoDiseño.id))
        serializer = DisenoSerializer(nuevoDiseño, many=False)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def send_proyecto(request, id_empresa):

    if request.method == 'POST':
        data = request
        body_unicode = request.body.decode('utf-8')
        proyecto = UserCustom.objects.get(id = id_empresa)
        body = json.loads(body_unicode)
	
        nuevoDiseño = Proyecto(
            nombre=body['nombre'],
            pago=body['pago'],
            empresa=proyecto,
            descripcion=body['descripcion']
        )
        nuevoDiseño.save()
        serializer = ProyectoSerializer(nuevoDiseño, many=False)
        return JsonResponse(serializer.data, safe=False)
