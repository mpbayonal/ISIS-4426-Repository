from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserCustomURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['id', 'url']


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class DisenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseno
        fields = '__all__'


class DisenoSinDetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseno
        email = serializers.EmailField()
        content = serializers.CharField(max_length=200)
        created = serializers.DateTimeField()

