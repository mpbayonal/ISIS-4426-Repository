# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
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
def get_data(request):
	data = Proyecto.objects.all()
	if request.method == 'GET':
		serializer = ProyectoSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)