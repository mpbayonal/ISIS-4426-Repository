from django.core.management.base import BaseCommand, CommandError

import datetime
import sendgrid
from datetime import timedelta
import io
import os

from django.utils.crypto import get_random_string
from boto3 import client, resource

from botocore.exceptions import ClientError
from celery.decorators import task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont

from backApp.models import Diseno


class Command(BaseCommand):

    def handle(self, *args, **options):

        logger = get_task_logger(__name__)

        s3_images_bucket = 'designmatch-grupo2'

        dynamodb = client('dynamodb', 'us-east-1',
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                          aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])



        sqs = client('sqs', 'us-east-1')
        cuantos = 0
        ya = False
        ya_inicio = False
        anterior = datetime.datetime.utcnow()
        while True:
            response = sqs.receive_message(
                QueueUrl='https://sqs.us-east-1.amazonaws.com/923905721779/designmatch-d')
            if 'Messages' in response:
                if ya_inicio == False:
                    inicio = datetime.datetime.utcnow()
                    anterior = inicio
                    ya_inicio = True
                else:
                    inicio = anterior
                for message in response['Messages']:
                    diseno_id = message['Body']
                    diseno = Diseno.get_id(diseno_id)['Items'][0]
                    s3 = resource('s3', 'us-east-1')
                    s3.Bucket(s3_images_bucket).download_file(
                        diseno['archivo'], '/tmp/' +
                        diseno['archivo'].replace('noProcesado/', ''))
                    img = Image.open(
                        '/tmp/'+diseno['archivo'].replace('noProcesado/', ''), "r")
                    img = Image.open(
                        '/tmp/'+diseno['archivo'].replace('noProcesado/', ''), "r")
                    imgResize = img.resize((800, 600), Image.ANTIALIAS)
                    draw = ImageDraw.Draw(imgResize)
                    draw.text((0, 580), "{0} {1} {2}".format(
                        diseno['nombre'], diseno['apellido'], diseno['fecha']), (0, 0, 0))
                    in_mem_file = io.BytesIO()
                    imgResize.save(in_mem_file, format='JPEG')
                    nombre = diseno['archivo'].replace(
                        'noProcesado/', 'disponible/')
                    try:
                        file_object = resource('s3').Object(
                            s3_images_bucket, nombre).last_modified
                        file_root, file_ext = os.path.splitext(nombre)
                        new_name = '{0}{1}{2}{3}'.format(
                            file_root, '_', get_random_string(), file_ext)
                        resource('s3').Bucket(s3_images_bucket).put_object(
                            Body=in_mem_file,
                            Key=new_name
                        )
                        Diseno.update(
                            diseno['apellido'],
                            diseno['nombre'],
                            diseno['pago'],
                            diseno['id'],
                            diseno['proyecto'],
                            diseno['fecha'],
                            diseno['archivo'],
                            new_name,
                            diseno['email'],
                            'Disponible')
                    except ClientError:
                        resource('s3').Bucket(s3_images_bucket).put_object(
                            Body=in_mem_file,
                            Key=nombre
                        )
                        Diseno.update(
                            diseno['apellido'],
                            diseno['nombre'],
                            diseno['pago'],
                            diseno['id'],
                            diseno['proyecto'],
                            diseno['fecha'],
                            diseno['archivo'],
                            nombre,
                            diseno['email'],
                            'Disponible')

                    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

                    data = {
                        "personalizations": [
                            {
                                "to": [
                                    {
                                        "email": [diseno['email']]
                                    }
                                ],
                                "subject": 'DesignMatch: Tus diseños ya están disponibles'
                            }
                        ],
                        "from": {
                            "email": 'je.bautista10@uniandes.edu.co'
                        },
                        "content": [
                            {
                                "type": "text/plain",
                                "value": 'Tu diseño ya está disponible\n\
                                                    http://d2b4n7yi665yz4.cloudfront.net/empresa/proyectos/diseños/' + diseno_id
                            }
                        ]
                    }

                    response = sg.client.mail.send.post(request_body=data)
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)





                    # Let the queue know that the message is processed
                    end = datetime.datetime.utcnow()
                    dynamodb.put_item(
                        TableName='modelo-d',
                        Item={
                            'origen': {'S': str(diseno_id)},
                            'fecha': {'S': str(datetime.datetime.utcnow())},
                            'tiempo': {'N': str((end-inicio).total_seconds())}
                        }
                    )
                    sqsr = resource('sqs', 'us-east-1')
                    message = sqsr.Message(
                        'https://sqs.us-east-1.amazonaws.com/923905721779/designmatch-d', message['ReceiptHandle'])
                    message.delete()
                    cuantos = cuantos + 1
                    if ya == False and (end-inicio).total_seconds() >= 60:
                        dynamodb.put_item(
                            TableName='cuantos-d',
                            Item={
                                'cuantos': {'N': str(cuantos)}
                            }
                        )
                        ya = True
                inicio = end
