
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import psycopg2
import datetime
import os
import dotenv

dotenv.read_dotenv()

start = datetime.datetime.utcnow()

query = 'select \
        nombre,\
        email,\
        estado,\
        fecha,\
        pago,\
        archivo,\
        apellido,\
        proyecto_id,\
        id \
    from \
        "backApp_diseno"  b\
    where \
        b.estado = \'No Procesado\''

connection = psycopg2.connect(user=os.getenv('RDS_USERNAME'),
                                password=os.getenv('RDS_PASSWORD'),
                                host=os.getenv('RDS_HOST'),
                                database=os.getenv('RDS_DATABASE'))

cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    nombre = row[0]
    email = row[1]
    estado = row[2]
    fecha = row[3]
    pago = row[4]
    url_archivo = row[5]
    apellido = row[6]
    proyecto_id = row[7]
    id_diseno = row[8]
    print(url_archivo)
    img = Image.open(url_archivo, "r")
    img.thumbnail((800, 600), Image.ANTIALIAS)
    draw = ImageDraw.Draw(img)
    draw.text((0, 600), "{0} {1}".format(nombre, apellido), (0, 0, 0))
    nombre_nuevo = url_archivo.split(".", 1)[0]+"_modificado."+url_archivo.split(".", 1)[1]
    img.save(nombre_nuevo)

    cursor.execute('UPDATE "backApp_diseno" set estado = %s, url_archivo_modificado = %s where id = %s', ("Disponible", nombre_nuevo, id_diseno))
    connection.commit()

end = datetime.datetime.utcnow()
print((end-start).total_seconds())
