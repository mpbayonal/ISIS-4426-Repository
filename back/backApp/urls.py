from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [



    path('getdata/', views.get_data),
    path('proyectos/', views.ListProyecto.as_view()),
    path('proyectos/<int:pk>/', views.DetailProyecto.as_view()),
    path('disenos/', views.ListDiseno.as_view()),
    path('disenos/<int:pk>/', views.DetailDiseno.as_view()),

    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),


    path(r'image', views.image),

    # url(r'^login/', views.login),
    # url(r'^&', views.index),

    # path('', views.index),

    # path('dashboard', views.dashboard),
    # path('logout', views.logout),

]