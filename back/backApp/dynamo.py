from .DynamoDBMapperMixin import *
from django.db import models

class modelAbstract(models.Model):
    """
    Basic abstract model for the rest of the models of the app
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["created_at"]


class Proyecto(DynamoDBMapperMixin, modelAbstract):

    DYNAMO_DB_TABLE = 'designmatch-proyectos'
    DYNAMO_DB_FIELDS = [
        'empresa', 'nombre', 'descripcion', 'pago'
    ]



class Diseno(DynamoDBMapperMixin, modelAbstract):

    DYNAMO_DB_TABLE = 'designmatch-disenos'
    DYNAMO_DB_FIELDS = [
        'nombre', 'apellido', 'email', 'estado', 'fecha', 'pago','archivo', 'url_archivo_modificado', 'proyecto'
    ]

