from . import views
from django.urls import path


urlpatterns = [

    path('proyecto/<urlLink>/', views.get_proyectos_Url),
    path('user/<pEmail>/', views.get_urlEmpresa_email),
    path('disenos/<proyecto_id>/', views.get_diseno_proyecto),
    path('proyectos/<pk>/', views.getProyectoById),
    path('proyectos/<pk>/eliminar/', views.eliminar_proyecto),
    path('proyectos/<pk>/editar/', views.editar_proyecto),
    path('diseno/<pk>/', views.getDisenoById),
    path('diseno/', views.send_diseno),
    path('proyectos/<email_empresa>/crear/', views.send_proyecto),
    path('auth/signup/', views.registro),
    path('auth/', views.login),
    path('', views.health),
    path('uploadkey/', views.get_upload_key)


]
