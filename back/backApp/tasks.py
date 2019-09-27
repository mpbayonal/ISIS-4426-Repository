import datetime
import io
import os

from boto3 import client
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont

from .models import Diseno

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="send_feedback_email_task",
    ignore_result=True
)
def process_image_and_send_mail():

    start = datetime.datetime.utcnow()
    disenos = Diseno.objects.filter(estado="No Procesado")

    for diseno in disenos:

        img = Image.open(diseno.archivo, "r")
        img.thumbnail((800, 600), Image.ANTIALIAS)
        draw = ImageDraw.Draw(img)
        draw.text((0, 580), "{0} {1}".format(
            diseno.nombre, diseno.apellido), (0, 0, 0))
        tempfile_io = io.BytesIO()
        img.save(tempfile_io, format='JPEG')
        image_file = InMemoryUploadedFile(
            tempfile_io, None, diseno.archivo.name, 'image/jpeg', tempfile_io.getbuffer().nbytes, None)
        diseno.url_archivo_modificado.save(diseno.archivo.name, image_file)
        diseno.estado = "Disponible"
        diseno.save()

        connection = client(
            'ses',
            'us-east-1',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
        )

        response = connection.send_email(
            Destination={
                'ToAddresses': [diseno.email]
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': 'Tus diseños ya están disponibles',
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
    print((end-start).total_seconds())
    return (end-start).total_seconds()
