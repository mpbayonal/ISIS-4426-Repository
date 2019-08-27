from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.urls import path

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [



    url(r'^getdata/', views.get_data),
    url(r'^$', views.HomePageView.as_view()),

    # url(r'^login/', views.login),
    # url(r'^&', views.index),

    # path('', views.index),

    # path('dashboard', views.dashboard),
    # path('logout', views.logout),

]