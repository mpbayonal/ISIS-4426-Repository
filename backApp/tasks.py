import datetime
import io
import os
from decimal import Decimal

from boto3 import client, resource
from celery.decorators import task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont

from .models import Diseno

logger = get_task_logger(__name__)

dynamodb = resource('dynamodb')

connection = client(
    'ses',
    'us-east-1',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
)

dynamodb_table = dynamodb.Table('modelo-c')

@task(
    name="send_feedback_email_task",
    ignore_result=True
)
def process_image_and_send_mail(id):
    
    start = datetime.datetime.utcnow()
    diseno = Diseno.objects.filter(id=id)[:1].get()
    img = Image.open(diseno.archivo, "r")
    imgResize = img.resize((800, 600), Image.ANTIALIAS)
    draw = ImageDraw.Draw(imgResize)
    draw.text((0, 580), "{0} {1} - {2}".format(
        diseno.nombre, diseno.apellido, diseno.fecha), (0, 0, 0))
    tempfile_io = io.BytesIO()
    imgResize.save(tempfile_io, format='JPEG')
    image_file = InMemoryUploadedFile(
        tempfile_io, None, diseno.archivo.name, 'image/jpeg', tempfile_io.getbuffer().nbytes, None)
    diseno.url_archivo_modificado.save(diseno.archivo.name, image_file)
    diseno.estado = "Disponible"
    diseno.save()

    response = connection.send_email(
        Destination={
            'ToAddresses': [diseno.email]
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'Tu diseño ya están disponible\n \
                    http://d1tprqpr49zo0i.cloudfront.net/empresa/proyectos/diseños/'+str(diseno.id),
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'DesignMatch: Tus diseños ya están disponibles',
            },
        },
        Source='je.bautista10@uniandes.edu.co',
    )
    end = datetime.datetime.utcnow()
    dynamodb_table.put_item(
            Item={
                'origen': diseno.id,
                'fecha': str(datetime.datetime.utcnow()),
                'tiempo': str((end-start).total_seconds())
            }
        )
    return (end-start).total_seconds()
