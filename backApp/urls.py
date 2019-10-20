from . import views
from django.urls import path


urlpatterns = [

    path('proyecto/<urlLink>/', views.get_proyectos_Url),
    path('user/<pUsername>/', views.get_url_email),
    path('disenos/<int:proyecto_id>/', views.get_diseno_proyecto),
    path('proyectos/<pk>/', views.getProyectoById),
    path('proyectos/<int:pk>/eliminar/', views.eliminar_proyecto),
    path('proyectos/<int:pk>/editar/', views.editar_proyecto),
    path('diseno/<pk>/', views.getDisenoById),
    path('diseno/', views.send_diseno),
    path('proyectos/<email_empresa>/crear/', views.send_proyecto),
    path('auth/signup/', views.registro),
    path('auth/', views.login),


]
