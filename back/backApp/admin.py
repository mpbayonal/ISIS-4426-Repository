# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Proyecto
from .models import Empresa
from .models import Diseño


# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Empresa)
admin.site.register(Diseño)