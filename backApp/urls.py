from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [

    path('proyecto/<urlLink>/', views.get_proyectos_Url),
    path('user/<pUsername>/', views.get_url_email),
    path('disenos/<int:proyecto_id>/', views.get_diseno_proyecto),
    path('proyectos/', views.ListProyecto.as_view()),
    path('proyectos/<int:pk>/', views.DetailProyecto.as_view()),
    path('disenos/', views.ListDiseno.as_view()),
    path('diseno/<int:pk>/', views.DetailDiseno.as_view()),
    path('diseno/', views.send_diseno),
    path('proyectos/<int:id_empresa>/crear/', views.send_proyecto),

    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),


    # url(r'^login/', views.login),
    # url(r'^&', views.index),

    # path('', views.index),

    # path('dashboard', views.dashboard),
    # path('logout', views.logout),

]