# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):

    nombre = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    user = models.ForeignKey(User, null=True , on_delete= models.CASCADE)
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    pago = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre


class Diseno(models.Model):

    nombre = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    estado = models.BooleanField()
    fecha = models.DateTimeField()
    pago = models.IntegerField()
    urlArchivo = models.CharField(max_length=500)
    proyecto = models.ForeignKey( Proyecto, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre


# Create your models here.
