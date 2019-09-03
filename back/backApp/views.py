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




import datetime
import os 
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


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class DetailDiseno(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diseno.objects.all()
    serializer_class = DisenoSerializer()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)


class Customers(TemplateView):
    def getCust(request):
        name = 'liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')


@csrf_exempt
def get_proyectos_Url(request, urlLink):

    if request.method == 'GET':

        user = UserCustom.objects.get(url = urlLink)
        data = Proyecto.objects.filter(empresa_id= user.id)
        serializer = ProyectoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def get_diseno_proyecto(request, proyecto_id):

    if request.method == 'GET':

        proyecto = Proyecto.objects.get(id = proyecto_id)
        data = Diseno.objects.filter(proyecto_id= proyecto.id)
        serializer = DisenoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def image(request):
    proyecto = Proyecto.objects.all().first()
    data = Diseno(fecha=datetime.datetime.utcnow)
    data.nombre = "test user"
    data.email = "test@user.com"
    data.estado = "No Procesado"
    data.fecha = datetime.datetime.utcnow()
    data.pago = "2500"
    data.urlArchivo = "./image.png"
    data.proyecto = proyecto
    if request.method == 'GET':
        img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '\\image.png', "r")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((0, 0), "Hola Mundo", (255, 255, 255))
        img.save('sample-out.png')
        serializer = DisenoSerializer(data, many=False)
        return JsonResponse(serializer.data, safe=False)
