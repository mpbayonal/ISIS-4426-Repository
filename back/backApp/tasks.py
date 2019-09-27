from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from .models import Diseno

import datetime

from boto3 import client

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
        nombre_nuevo = url_archivo.split(
            ".", 1)[0]+"_modificado."+url_archivo.split(".", 1)[1]
        img.save(nombre_nuevo)
        diseno.url_archivo_modificado = diseno.archivo
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
