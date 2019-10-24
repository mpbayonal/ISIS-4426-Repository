from django.core.management.base import BaseCommand, CommandError

import datetime
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
                        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

        connection = client(
            'ses',
            'us-east-1',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        while True:
            sqs = client('sqs', 'us-east-1')
            response = sqs.receive_message(
                QueueUrl='https://sqs.us-east-1.amazonaws.com/547712166517/designmatch-d')
            if 'Messages' in response:
                for message in response['Messages']:
                    start = datetime.datetime.utcnow()
                    diseno_id = message['Body']
                    diseno = Diseno.get_id(diseno_id)['Items'][0]
                    s3 = resource('s3')
                    s3.Bucket(s3_images_bucket).download_file(
                        diseno['archivo'], '/tmp/' +
                            diseno['archivo'].replace('noProcesado/', ''))
                    img=Image.open('/tmp/'+diseno['archivo'].replace('noProcesado/', ''), "r")
                    imgResize=img.resize((800, 600), Image.ANTIALIAS)
                    draw=ImageDraw.Draw(imgResize)
                    draw.text((0, 580), "{0} {1} {2}".format(
                        diseno['nombre'], diseno['apellido'], diseno['fecha']), (0, 0, 0))
                    in_mem_file=io.BytesIO()
                    imgResize.save(in_mem_file, format='JPEG')
                    in_mem_file.seek(0)
                    nombre=diseno['archivo'].replace(
                        'noProcesado/', 'disponible/')
                    try:
                        file_object=resource('s3').Object(
                            s3_images_bucket, nombre).last_modified
                        file_root, file_ext=os.path.splitext(nombre)
                        new_name='{0}{1}{2}{3}'.format(
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

                    response=connection.send_email(
                        Destination={
                            'ToAddresses': [diseno['email']]
                        },
                        Message={
                            'Body': {
                                'Text': {
                                    'Charset': 'UTF-8',
                                    'Data': 'Tu diseño ya está disponible\n\
                                http://d2b4n7yi665yz4.cloudfront.net/empresa/proyectos/diseños/'+diseno_id,
                                },
                            },
                            'Subject': {
                                'Charset': 'UTF-8',
                                'Data': 'DesignMatch: Tus diseños ya están disponibles',
                            },
                        },
                        Source='je.bautista10@uniandes.edu.co',
                    )
                    end=datetime.datetime.utcnow()
                    dynamodb.put_item(
                        TableName='modelo-d',
                        Item={
                            'origen': {'S': str(diseno_id)},
                            'fecha': {'S': str(datetime.datetime.utcnow())},
                            'tiempo': {'N': str((end-start).total_seconds())}
                        }
                    )
                    # Let the queue know that the message is processed
                    sqs=resource('sqs', 'us-east-1')
                    message=sqs.Message(
                        'https://sqs.us-east-1.amazonaws.com/547712166517/designmatch-d', message['ReceiptHandle'])
                    message.delete()
