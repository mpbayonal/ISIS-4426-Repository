from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class DiseñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseño
        fields = '__all__'

