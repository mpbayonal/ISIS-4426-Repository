import base64
import os
import bcrypt
import jwt
import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.core import serializers

from rest_framework.utils import json



from .models import *


# path('proyecto/<urlLink>/', views.get_proyectos_Url),
# path('user/<pUsername>/', views.get_url_email),
# path('disenos/<int:proyecto_id>/', views.get_diseno_proyecto),

# path('proyectos/', views.ListProyecto.as_view()),
# path('proyectos/<int:pk>/', views.DetailProyecto.as_view()),

# path('diseno/<int:pk>/', views.getDisenoById),
# path('diseno/', views.send_diseno),
# path('proyectos/<int:id_empresa>/crear/', views.send_proyecto),
#
# path('auth/', include('rest_auth.urls')),
# path('auth/signup/', include('rest_auth.registration.urls')),




    # def create(self, request, *args, **kwargs): # don't need to `self.request` since `request` is available as a parameter.
    #     serializer = self.serializer_class(request.data)
    #     data = serializer.data
    #     os.mkdir(data['nombre'])
    #     return JsonResponse(serializer.data, safe=False)





#     path('diseno/<int:pk>/', views.getDisenoById),
@csrf_exempt
def getDisenoById(request, pk):
    data = serializers.serialize("json", Diseno.objects.filter(pk=pk))
    return HttpResponse(data)

#     path('proyectos/<int:pk>/', views.getProyectoById),
@csrf_exempt
def getProyectoById(request, pk):

    data = serializers.serialize("json", Proyecto.objects.filter(pk=pk))

    return HttpResponse(data)




#     path('proyectos/<int:pk>/editar/', views.editar_proyecto),
@csrf_exempt
def editar_proyecto(request, pk):

    if request.method == 'POST':
        data = request
        body_unicode = request.body.decode('utf-8')
        proyecto = Proyecto.objects.get(id = pk)
        body = json.loads(body_unicode)
        print(body)

        proyecto.nombre = body['nombre']
        proyecto.pago=body['pago']
        proyecto.empresa=proyecto
        proyecto.descripcion=body['descripcion']

        proyecto.save()
        data = serializers.serialize("json", Proyecto)

        return HttpResponse(data)



#     path('proyectos/<int:pk>/eliminar/', views.eliminar_proyecto),
@csrf_exempt
def eliminar_proyecto(request, pk):

    if request.method == 'POST':
        proyecto = Proyecto.objects.filter(pk = pk).delete()
        return HttpResponse(status=204)







# path('proyecto/<urlLink>/', views.get_proyectos_Url),
@csrf_exempt
def get_proyectos_Url(request, urlLink):

    if request.method == 'GET':

        user = UserCustom.objects.get(url = urlLink)
        proyecto = Proyecto.objects.filter(empresa_id= user.id)
        data = serializers.serialize("json", proyecto)

        return HttpResponse(data)


#     path('disenos/<int:proyecto_id>/', views.get_diseno_proyecto),
@csrf_exempt
def get_diseno_proyecto(request, proyecto_id):

    if request.method == 'GET':

        proyecto = Proyecto.objects.get(id = proyecto_id)
        disenos = Diseno.objects.filter(
            proyecto_id= proyecto.id).filter(
                estado="Disponible")
        data = serializers.serialize("json", disenos)
        return HttpResponse(data)

#     path('user/<pUsername>/', views.get_url_email),
@csrf_exempt
def get_url_email(request, pUsername):

    if request.method == 'GET':
        user = UserCustom.objects.get(username = pUsername)
        user.url = user.username + "" + str(user.id)
        user.save()
        data = serializers.serialize("json", user)
        return HttpResponse(data)

#     path('diseno/', views.send_diseno),
@csrf_exempt
def send_diseno(request):

    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        input_image = files['image']
        proyecto = Proyecto.objects.get(id = data['proyecto'])

        nuevoDiseño = Diseno(
            nombre=data['nombre'],
            apellido=data['apellido'],
            email=data['email'],
            estado=data['estado'],
            pago=data['pago'],
            proyecto=proyecto,
            archivo=input_image
        )
        nuevoDiseño.save()
        data = serializers.serialize("json", nuevoDiseño)
        return HttpResponse(serializers.serialize("json" , data))




#     path('proyectos/<int:id_empresa>/crear/', views.send_proyecto),

@csrf_exempt
def send_proyecto(request, id_empresa):

    if request.method == 'POST':
        data = request
        body_unicode = request.body.decode('utf-8')
        empresa = UserCustom.get_id(id_empresa)
        body = json.loads(body_unicode)
        print(body)

        nuevoProyecto = Proyecto(
            nombre=body['nombre'],
            pago=body['pago'],
            empresa=empresa,
            descripcion=body['descripcion']
        )
        nuevoProyecto.save()
        data = serializers.serialize("json", nuevoProyecto)

        return HttpResponse(data)


@csrf_exempt
def registro(request):

    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')

        body = json.loads(body_unicode)
        empresa = UserCustom.get_email(body['email'])

        print(empresa['Count'] > 0)
        if empresa['Count'] > 0:
            return HttpResponse(status=409)

        if body['password2'] != body['password1']:
            return HttpResponse(status=401)

        else:
            password = body['password1']
            b = password.encode('utf-8')  # I just added this line
            password_encrypt = bcrypt.hashpw(b, bcrypt.gensalt())

            empresa = UserCustom()
            empresa.Username = body['username']
            empresa.Password = password_encrypt
            empresa.Email = body['email']
            empresa.save()

            data = serializers.serialize("json", empresa)
            return HttpResponse(data)

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

@csrf_exempt
def login(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')

        body = json.loads(body_unicode)
        empresa = UserCustom.get_email(body['email'])



        if empresa['Count'] < 1 :
            return HttpResponse(status=404)


        password = body['password'].encode('utf-8')

        passwordHash = empresa['Items'][0]['password'].value


        if bcrypt.checkpw(password, passwordHash) == False:
            return HttpResponse(status=401)

        else:

            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=900),
                'iat': datetime.datetime.utcnow(),
                'sub': empresa['Items'][0]['id']
            }
            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm='HS256'
            )

            #payload = jwt.decode(auth_token, settings.SECRET_KEY)

           

            UserCustom.update( empresa['Items'][0]['email'], 'token' , token )



            data = serializers.serialize("json", empresa)
            return HttpResponse(data)
