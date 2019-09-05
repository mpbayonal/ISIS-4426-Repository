# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime

class UserCustom(AbstractUser):

    url = models.CharField(max_length=500, default= "url")
    # add additional fields in here


# class Empresa(models.Model):
#
#
#     url = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.nombre



class Proyecto(models.Model):
    empresa = models.ForeignKey(settings.AUTH_USER_MODEL , null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    pago = models.IntegerField()

    def __str__(self):
        return self.nombre


class Diseno(models.Model):

    nombre = models.CharField(max_length=500)
    apellido = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    estado = models.CharField(max_length=500)
    fecha = models.DateTimeField(default=datetime.datetime.utcnow)
    pago = models.IntegerField()
    url_archivo = models.CharField(max_length=500)
    proyecto = models.ForeignKey( Proyecto, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre


# Create your models here.
