# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Proyecto


from .models import Diseno
from .models import UserCustom


# Register your models here.
admin.site.register(Proyecto)
admin.site.register(UserCustom)

admin.site.register(Diseno)